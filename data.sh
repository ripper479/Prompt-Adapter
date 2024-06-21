pip install gdown

DATA= /content/DATA
mkdir $DATA

cd $DATA

# pip install gdown

mkdir -p caltech-101
cd caltech-101
# wget http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz 
wget https://data.caltech.edu/records/mzrjq-6wc02/files/caltech-101.zip
unzip caltech-101.zip
mv caltech-101/101_ObjectCategories.tar.gz .
gdown 1hyarUivQE36mY6jSomru6Fjd-JzwcCzN
tar -xvf 101_ObjectCategories.tar.gz 
cd $DATA

mkdir -p oxford_pets
cd oxford_pets
wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz
gdown  1501r8Ber4nNKvmlFVQZ8SeUHTcdTTEqs
tar -xvf images.tar.gz
tar -xvf annotations.tar.gz
cd $DATA

wget https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/archives/fgvc-aircraft-2013b.tar.gz
tar -xvf fgvc-aircraft-2013b.tar.gz
mv fgvc-aircraft-2013b/data fgvc_aircraft
cd $DATA


wget https://www.robots.ox.ac.uk/~vgg/data/dtd/download/dtd-r1.0.1.tar.gz
tar -xvf dtd-r1.0.1.tar.gz
cd dtd
gdown 1u3_QfB467jqHgNXC00UIzbLZRQCg2S7x
cd $DATA

mkdir -p eurosat
cd eurosat
wget http://madm.dfki.de/files/sentinel/EuroSAT.zip
unzip EuroSAT.zip
gdown 1Ip7yaCWFi0eaOFUGga0lUdVi_DDQth1o
cd $DATA

mkdir -p ucf101
cd ucf101
gdown  10Jqome3vtUA2keJkNanAiFpgbyC9Hc2O
unzip UCF-101-midframes.zip
gdown 1I0S0q91hJfsV9Gf4xDIjgDq4AqBNJb1y
cd $DATA
