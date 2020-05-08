# This is bash code, the same language in your ~/.bash_profile and ~/.bashrc 

# The following will put your desktop on your PATH, and the following to your 
# PYTHONPATH. Note that $HOME refers simply to your home directory, the same 
# as a '~' sign. 

export PATH=$HOME/Desktop:$PATH 

export PYTHONPATH=$HOME/Desktop:$PYTHONPATH 

# $PATH and $PYTHONPATH must be at the end in order to append any directories 
# already on your PATH and PYTHONPATH to its new value. Otherwise they will 
# be removed from your PATH/PYTHONPATH. This can cause a wide range of 
# problems if you forget this. 

# Take special note that your PATH and your PYTHONPATH are just specific 
# environment variables, just like EXAMPLE in these exercises. 

# This change will be permanent as long as this line remains in the file you 
# put it into. To get rid of it, simply delete the line and restart your 
# terminal. 
