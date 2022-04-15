for x in $(cat requirements.txt); 
    do $x sudo apt-get install $x; 
done

pip install plotly
pip install --upgrade nbformat

