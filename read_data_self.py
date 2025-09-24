from PIL import Image
import os
from torch.utils.data import Dataset



class MyDataset(Dataset):
    def __init__(self,root_dir,label_dir):
        self.root_dir=root_dir
        self.label_dir=label_dir
        self.path=os.path.join(self.root_dir,self.label_dir)
        self.img_names=os.listdir(self.path)

    def __getitem__(self, item):
        img_name=self.img_names[item]
        img_item_path=os.path.join(self.root_dir,self.label_dir,img_name)
        img=Image.open(img_item_path)
        label=self.label_dir
        return img,label

    def __len__(self):
        return len(self.img_path)

root_dir="dataset/train"
ants_label_dir1="ants"
bees_label_dir1="bees"
ants_dataset1=MyDataset(root_dir,ants_label_dir1)
bees_dataset1=MyDataset(root_dir,bees_label_dir1)
img,label=ants_dataset1[1]
img.show()
