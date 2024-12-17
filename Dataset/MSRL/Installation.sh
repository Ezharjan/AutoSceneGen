conda create -n msrl python=3.7 -y
conda activate msrl
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge -y
pip install -r requirements.txt
pip install tensorboard

python trainvae.py