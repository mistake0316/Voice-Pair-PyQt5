from model_backend import YidarConvert 
import json
from collections import namedtuple
import shutil
import os

if __name__ == "__main__":
    config = json.load(open("config.json","r"))
    convert_config =  config["convert_config"]
    convert_config["src_spk"] = "cyan"
    convert_config["trg_spk"] = "p272"
    convert_config["num_converted_wavs"] = 4

    argv = namedtuple("argv", convert_config.keys())(*convert_config.values())
    YidarConvert.test_Yidar(argv)
    
    
