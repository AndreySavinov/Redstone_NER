# Redstone_NER
Simple client-server interface for NER
# Requirements
### Linux 
#### AWS web-server, Spacy
Unfortunately, free EC2 instance on AWS does not have enough memoty to install pretrained models.
This `runner_aws.sh` installs Spacy library for NER
- `cd server`
- `chmod +x runner_aws.sh`
- `./runner_aws.sh`

#### BERT-NER [Source](https://github.com/kamalkraj/BERT-NER)
I run this model on my laptop. 
This `runner_bert.sh` clones BERT-NER and installs prerequirements for it. 
- `cd server`
- `chmod +x runner_bert.sh`
- `./runner_bert.sh`

 Pretrained model can be downloaded from [here](https://1drv.ms/u/s!Auc3VRul9wo5hghurzE47bTRyUeR?e=08seO3), unzip archieve and put the folder `out_base` into `BERT-NER`
 
### Windows

#### Spacy
python3 -m spacy download en_core_web_sm
- `pip install -U spacy`
- `python3 -m spacy download en_core_web_sm`
- 
#### BERT-NER [Source](https://github.com/kamalkraj/BERT-NER)
 - `git clone https://github.com/kamalkraj/BERT-NER.git` for BERT-NER from the folder `server`
 - `pip install -r requirements.txt` from the folder `BERT-NER`
  
 
 
