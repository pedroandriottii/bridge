## Nosso projeto

O bridge é uma ferramenta inovadora desenvolvida para auxiliar o nosso cliente: Os caçadores de bons exemplos, a gerenciar seus projetos e facilitar sua comunicação com as ONGs que solicitam sua ajuda e seus 88 embaixadores. É desenvolvido por alunos do terceiro período de ciência da computação, para a cadeira de projetos.

![Progress](https://progress-bar.dev/100/?title=completed)

## Como Rodar

1. Primeiramente, é necessário clonar o repositório através do comando "git clone <url do repositório>". em seguida, precisamos acessar a pasta do repositório com o comando "cd bridge-projetos".
![image](https://github.com/edmaaralencar/bridge-projetos/assets/117591564/1fbca312-9734-4b2b-bf09-5488720aa5a0)

3. Em seguida, é necessário instalar todos os pacotes necesários para abrir o servidor localmente. Podemos fazer isso com o simples comando "pip install -r requirements.txt".
![image](https://github.com/edmaaralencar/bridge-projetos/assets/117591564/c60560c9-7caf-4a56-a9e7-8cda90290e70)

4. Agora, precisamos acessar o diretório onde está nosso projeto, com o comando "cd project".
![image](https://github.com/edmaaralencar/bridge-projetos/assets/117591564/5421a28a-c3fa-408c-ae46-bc129982bfb7)

5. Finalmente, podemos rodar o server com o comando "python manage.py runserver". basta então clicar no link de servidor local.
![image](https://github.com/edmaaralencar/bridge-projetos/assets/117591564/cbb74392-e83a-4c7a-afbe-fabb43308893)

   
## Funcionalidades

Nosso software contará com três logins: 

Gestores: Supervisionam cada projeto cadastrado no sistema, e possibilitarão os cadastros de novos embaixadores e gestores para a rede.

Usuários: Poderão solicitar a ajuda dos caçadores por meio de um simples formulário com informações do projeto e suas demandas.

Embaixadores: Serão responsáveis pela triagem dos projetos e seu acompanhamento, relatando seus avanços na página KanBan do projeto.

Ademais, o sistema também possui um mural atualizado automáticamente com vários marcos do projeto, disponibilizando tal informação para os gestores.


# Como usar (IMPORTANTE)

## Gestor:
**Nota:** O gestor não pode ser cadastrado imediatamente. Apenas gestores têm permissão para cadastrar novos gestores. Para acessar as histórias seguintes, utilize as seguintes credenciais de login:
- **Usuário:** Camila
- **Senha:** Teste.123

1. Após o login, o usuário gestor pode cadastrar novos gestores e embaixadores através da opção "cadastrar" na navbar.
2. Visualize todas as demandas no sistema e busque por elas utilizando o nome através da opção de busca na tela inicial.
3. Selecione "ver todos" para acessar o quadro kanban e movimentar as demandas dentro desse quadro.
4. Para mover uma demanda, clique no círculo com '>' no canto direito de cada card. Detalhes serão mostrados, e você pode atualizar o andamento através da opção "Atualizar andamento".

## Embaixador:
**Nota:** O embaixador não pode ser cadastrado imediatamente. Apenas gestores podem cadastrar novos embaixadores. Para acessar as histórias seguintes, utilize as seguintes credenciais de login:
- **Usuário:** AnaOliveira
- **Senha:** Teste.123

1. Deixe sua tela de navegador em modo de inspeção ou selecione a tecla "f12". Em seguida, alterne o tipo de exibição para o de um celular.
2. Após o login, o usuário embaixador pode acessar demandas e atualizar o andamento delas. Basta selecionar o card, escolher o novo status através do box no meio da tela e, em seguida, clicar em "atualizar".
3. Demandas em processo de triagem aparecerão na opção "triagem" da navbar. Lá, o embaixador pode aprovar ou não projetos de sua região. Caso aprovados, eles aparecerão na tela "inicio".
4. Para encerrar uma demanda, basta atualizar seu status como "concluído". Essa ação refletirá na aba "Feed", onde veremos atualizações de todos os embaixadores.

## Usuário:
1. Na tela inicial do localhost, clique na opção "Cadastre sua ONG".
2. Preencha o formulário.
3. Crie uma nova demanda, pressionando o botão + próximo ao seu nome.
4. Cadastre uma nova demanda.
5. Agora, você pode acompanhar o andamento do seu pedido!



## Integrantes

<table>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://github.com/arthurreis33">
          <img src="https://github.com/arthurreis33.png" width="100" alt="foto" style="max-width: 100px;">
          <br>
          <sub>
            Arthur Reis
          </sub>
          <br>
          <sub>
            aars@cesar.school
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/pedroandriottii">
          <img src="https://github.com/pedroandriottii.png" width="100" alt="foto" style="max-width: 100px;">
          <br>
          <sub>
            Pedro Andriotti
          </sub>
          <br>
          <sub>
            phab@cesar.school
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/CarlosAugustoP">
          <img src="https://github.com/CarlosAugustoP.png" width="100" alt="foto" style="max-width: 100px;">
          <br>
          <sub>
            Carlos Augusto
          </sub>
          <br>
          <sub>
            capvf@cesar.school
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/grossiter04">
          <img src="https://github.com/grossiter04.png" width="100" alt="foto" style="max-width: 100px;">
          <br>
          <sub>
            Gabriel Rossiter
          </sub>
          <br>
          <sub>
            gsr@cesar.school
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/edmaaralencar">
          <img src="https://github.com/edmaaralencar.png" width="100" alt="foto" style="max-width: 100px;">
          <br>
          <sub>
            Edmar Alencar
          </sub>
          <br>
          <sub>
            era@cesar.school
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/luismingati">
          <img src="https://github.com/luismingati.png" width="100" alt="foto" style="max-width: 100px;">
          <br>
          <sub>
            Luis Otavio
          </sub>
          <br>
          <sub>
            locm@cesar.school
          </sub>
        </a>
      </td>
    </tr>
  </tbody>
</table>
