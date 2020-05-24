echo Creating dataset folder structure...
cd ..
mkdir dataset
cd dataset
mkdir COCO
cd COCO
echo Cloning COCO API...
git clone https://github.com/gineshidalgo99/cocoapi.git
cd cocoapi
mkdir images
mkdir annotations
cd ..
echo Creating required folders in dataset/COCO/...
mkdir json
mkdir mat
exit