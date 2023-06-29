import requests
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"

print(RED+'''
                                                                                                                                  
                                    bbbbbbbb                                                                                      
   SSSSSSSSSSSSSSS                  b::::::b               SSSSSSSSSSSSSSS                                                        
 SS:::::::::::::::S                 b::::::b             SS:::::::::::::::S                                                       
S:::::SSSSSS::::::S                 b::::::b            S:::::SSSSSS::::::S                                                       
S:::::S     SSSSSSS                  b:::::b            S:::::S     SSSSSSS                                                       
S:::::S            uuuuuu    uuuuuu  b:::::bbbbbbbbb    S:::::S                cccccccccccccccc  aaaaaaaaaaaaa  nnnn  nnnnnnnn    
S:::::S            u::::u    u::::u  b::::::::::::::bb  S:::::S              cc:::::::::::::::c  a::::::::::::a n:::nn::::::::nn  
 S::::SSSS         u::::u    u::::u  b::::::::::::::::b  S::::SSSS          c:::::::::::::::::c  aaaaaaaaa:::::an::::::::::::::nn 
  SS::::::SSSSS    u::::u    u::::u  b:::::bbbbb:::::::b  SS::::::SSSSS    c:::::::cccccc:::::c           a::::ann:::::::::::::::n
    SSS::::::::SS  u::::u    u::::u  b:::::b    b::::::b    SSS::::::::SS  c::::::c     ccccccc    aaaaaaa:::::a  n:::::nnnn:::::n
       SSSSSS::::S u::::u    u::::u  b:::::b     b:::::b       SSSSSS::::S c:::::c               aa::::::::::::a  n::::n    n::::n
            S:::::Su::::u    u::::u  b:::::b     b:::::b            S:::::Sc:::::c              a::::aaaa::::::a  n::::n    n::::n
            S:::::Su:::::uuuu:::::u  b:::::b     b:::::b            S:::::Sc::::::c     ccccccca::::a    a:::::a  n::::n    n::::n
SSSSSSS     S:::::Su:::::::::::::::uub:::::bbbbbb::::::bSSSSSSS     S:::::Sc:::::::cccccc:::::ca::::a    a:::::a  n::::n    n::::n
S::::::SSSSSS:::::S u:::::::::::::::ub::::::::::::::::b S::::::SSSSSS:::::S c:::::::::::::::::ca:::::aaaa::::::a  n::::n    n::::n
S:::::::::::::::SS   uu::::::::uu:::ub:::::::::::::::b  S:::::::::::::::SS   cc:::::::::::::::c a::::::::::aa:::a n::::n    n::::n
 SSSSSSSSSSSSSSS       uuuuuuuu  uuuubbbbbbbbbbbbbbbb    SSSSSSSSSSSSSSS       cccccccccccccccc  aaaaaaaaaa  aaaa nnnnnn    nnnnnn

'''+WHITE)


subdominios=["backup","teste","sl","email","admin","adm","interno"]

alvo=input(YELLOW+"insira seu alvo: ")
print("escaneando alvo...")

for index in subdominios:
    site="https://"+index+"."+alvo
    try:
        requisicao = requests.get(site)
        print(GREEN+"***** subdominio encontrado! *****"+WHITE+" | "+site)        
    except:
        print(RED+"Subdominio não encontrado"+WHITE+" | "+site)