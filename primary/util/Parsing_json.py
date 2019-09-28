import json
class Parsing_Json():
    def parsing_monolayer(self,file,key):
        try:
            with open(file,'r',encoding='utf-8') as f:
               content = json.loads(f.read())
               if content:
                   if key in content:
                        return content[key]
        except Exception as e:
            raise e

    # def parsing_strategy_locator(self,file,page,element):
    #     try:
    #         with open(file,'r',encoding='utf-8') as f:
    #            content = json.loads(f.read())
    #            if content:
    #                if page in content:
    #                     if element in content[page]:
    #                         return content[page][element]
    #     except Exception as e:
    #         raise e

    def parsing_strategy_locators(self, file, page, element):
        try:
            content = self.parsing_monolayer(file,page)
            if content:
                if element in content:
                        return content[element]
        except Exception as e:
            raise e

