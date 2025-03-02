from configparser import ConfigParser

class Config:
    def __init__(self, config_file='./src/langgraphagenticai/config.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)
    
    def get_llm_option(self):
        #return self.config['DEFAULT']['LLM_OPTIONS']
        return self.config['DEFAULT'].get('LLM_OPTIONS')
    
    def get_usecase_options(self):
        return self.config['DEFAULT'].get('USECASE_OPTIONS')
    
    def get_model_options(self):
        return self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS')

