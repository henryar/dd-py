from ddpy.interfaces.ddan import DDAN


ddan = DDAN(api_key="", analyzer_ip="")
resp = ddan.submit_file('/Users/jeff/Desktop/word_sample_20180222145346.doc')
print(resp)

