import torch
import torch.nn as nn 
import torchvision.transforms.functional as TF
class DoubleConv(nn.Module):
    def __init__(self, in_channel,out_channel):
        super(DoubleConv,self).__init__()
        self.conv = nn.Sequential(
        nn.Conv2d(in_channel,out_channel,3,1,1,bias= False),
        nn.BatchNorm2d(out_channel),
        nn.ReLU(inplace = True),
        nn.Conv2d(out_channel,out_channel,3,1,1,bias= False),
        nn.BatchNorm2d(out_channel),
        nn.ReLU(inplace = True)
        )
    def forward(self,x):
        return self.conv(x)
        

class U_Net(nn.Module):
    def __init__(self,in_channel=3,out_channel=1,features =[64,128,256,512]):
        super(U_Net,self).__init__()
        self.downs = nn.ModuleList()
        self.ups = nn.ModuleList()
        self.pool = nn.MaxPool2d(2,2)

        ### for downs 
        for feature in features:
            self.downs.append(DoubleConv(in_channel,feature))
            in_channel = feature
        ##for ups 
        for feature in reversed(features):
            self.ups.append(nn.ConvTranspose2d(feature*2,feature,kernel_size = 2, stride = 2))
            self.ups.append(DoubleConv(feature*2,feature))
        self.bottleneck = nn.Conv2d(features[-1],features[-1]*2,3,1,1)
        self.final_conv = nn.Conv2d(features[0],out_channel,3,1,1)

    def forward(self,x):
        ### for down 
        skip_connections = []
        for down in self.downs: 
            x = down(x)
            skip_connections.append(x)
            x = self.pool(x)
        x = self.bottleneck(x)
        ### for up 
        skip_connections = skip_connections[::-1]
        for idx in range(0,len(self.ups), 2):
            x = self.ups[idx](x)
            skip_connection = skip_connections[idx//2]
            if x.shape!= skip_connection.shape:
                x= TF.resize(x,size= skip_connection.shape[2:])
            skip_value = torch.cat((skip_connection,x),dim=1)
            x= self.ups[idx+1](skip_value)
        return self.final_conv(x)
    
    
def Test():
    print("test")
    x = torch.randn(3,1,190,190)
    model = U_Net(in_channel= 1, out_channel=1)
    preds = model(x)
    print(preds.shape)

if __name__=="__main__":
    Test()