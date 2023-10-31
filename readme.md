#### Committer

#### Descrição 

O commiter é um software para utilizar em atualizações automáticas de códigos 
de projeto, assim o desenvolvedor não precisa ficar dando git pull toda hora e
nem enviando código toda hora para o repositório.

Ele também pode ser utilizado para fazer o 
deploy automático de projetos, em locais onde é problemático ter acesso toda hora, 
ou é necessário pedir acesso a terceiros para efetuar o deploy de um projeto.

##### pyinstaller

Para executar o install.sh será necessário ter o pyinstaller instalado no seu sistema
operacional. Há várias maneiras de fazer isso, porém irei passar somente uma forma 
de fazer isso, se você souber de outras maneiras, fique à vontade de fazer da 
maneira que achar melhor, desde que saiba o que está fazendo.

    ~# apt-get update
    ~# apt-get install python3-pip
    ~# apt-get install python3-venv
    ~# cd /opt
    ~# python3 -m venv venv
    ~# source venv/bin/activate
    (venv)~# pip install --upgrade pip
    (venv)~# pip install pyinstaller
    (venv)~$ deactivate
    ~# ln -s /opt/venv/bin/pyinstaller /usr/bin/pyinstaller

#### installer.sh

    ~# git clone git@github.com:elipe-pereira/committer.git
    ~# cd committer
    ~# chmod +x installer.sh

Os comandos acima baixam o projeto, acessa a pasta e dá permissão de execução
ao script installer.sh

    ~# ./installer.sh pack

Compila o programa e faz o empacotamento gerando ao final da execução um arquivo
committer_x.x.x_amd64.deb. Para instalar o arquivo gerado basta executar o comando: 

    ~# apt-get install ./committer_x.x.x_amd64.deb

Caso sua intenção seja somente compilar o programa, execute o comando: 

    ~# ./installer.sh build

Este comando fará somente a compilação do programa e a pasta com o programa compilado
será armazenado em /tmp/build/dist/committer. Basta acessar a pasta e executar o programa
compilado seja para fins de teste, seja para uso geral. 

    ~# ./installer.sh clear

O comando acima apaga a pasta de build (/tmp/build) onde ficam armazenados o código
compilado e a pasta com os arquivos temporários resultatntes da compilação, além do 
arquivo .spec gerado e que também pode ser utilizado para compilações futuras caso
você utilize o pyinstaller diretamente. 

    ~# ./installer.sh help

O comando acima exibe uma mensagem de ajuda, assim como executar o comando installer
sem nenhum parâmetro também causará a exibição da mesma mensagem de ajuda. 