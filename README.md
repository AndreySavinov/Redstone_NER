# Redstone_NER
Simple client-server interface for NER
# Requirements
### Linux 
#### AWS web-server
Unfortunately, free EC2 instance on AWS does not have enough memoty to install pretrained models.
This `runner_aws.sh` installs Spacy library for NER
- `cd server`
- `chmod +x runner_aws.sh`
- `./runner_aws.sh`

#### BERT-NER [Source](https://github.com/kamalkraj/BERT-NER)
I run this model on my laptop. 
This `runner_aws.sh` installs Spacy library for NER
- `cd server`
- `chmod +x runner_bert.sh`
- `./runner_bert.sh`

 Pretrained model download from [here](https://1drv.ms/u/s!Auc3VRul9wo5hghurzE47bTRyUeR?e=08seO3), unzip archieve and put the folder `out_base` into `BERT-NER`
