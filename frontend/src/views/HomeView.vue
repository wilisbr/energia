<template>
  <div class="container">
    <div class="content is-normal has-text-justified" >
      <p> Este sistema, de uso gratuiro, possbilita uma gestão <strong>eficiente</strong> para quem possui sistema de 
      geração distribuída e trasfere o excedente para outras instalações, recebendo, 
      em contrapartida, uma compensação financeira. O objetivo do sistema é automatizar todo o cálculo e a geração da cobrança 
      para o seu cliente. O sistema torna tudo muito simples e rápido, de modo que você configura poucos parâmetros (ex: % de desconto) e 
      faz o upload da conta de luz no formato PDF (o arquivo deverá ser baixado do site da CEMIG). Com poucos segundos 
      você terá em mãos um documento explicando ao seu cliente o quanto ele economizou e quanto dele deverá te pagar.</p>
      

      <h2> Instruções de uso </h2>

      <h3>1) Cadastrando as Instalações</h3>
      <p> No menu superior, acesse a opção "Instalações" e cadastre as instalações dos seus clientes.</p>
      <p>Uma das oções é o <strong>desconto</strong>, onde o usuário irá definir qual o percentual de desconto,
       em relação ao preço da concessionária. Ex: se a concessionária cobra R$ 1,00 por kwh,
       o usuário que definir 20% de desconto, estará cobrando R$ 0,80 centavos do cliente, por KWh.</p>
      <p> Outra opção importante é o <strong> bônus </strong>, que corresponde a um desconto absoluto e incondicional que
        será aplicado no faturamento do seu cliente. Recomendamos deixar o campo com valor 0, inicialmente</p>

      <h3>2) Fazendo upload das contas </h3>
      <p> Após incluir a instalação do seu cliente, acesso a opção <strong>Faturas</strong> no menu superior, 
      escolha a instalação desejada e faça o upload da fatura. Importante ressaltar que o sistema só vai 
      reconhecer faturas baixadas <strong>diretamente do site da Cemig</strong>, no formato PDF. Estamos 
      trabalhando para adicionar outras concessionárias. A próxima a ser incluída será a Enel</p>

      <h3>3) Geração da cobrança</h3>
      <p>Escolha uma das faturas que foram incluídas e clique na opção <strong>Faturar</strong>. Faça o download
      e envie para seu cliente!</p>

      Caso você precise fazer uma gestão completa, incluindo prospecção de clientes, relacionamento e cobrança, entre
      em contato para firmarmos uma paceria <strong>(cwgestao@aol.com).</strong> Caso você opte por fazer todo o trabalho, 
      sinta-se livre para utilizar este sistema de forma <strong>gratuita.</strong>

    </div>
  </div>

    

</template>

<script>
/* eslint-disable */
import axios from 'axios'
 
export default {
  name: 'HomeView',
  data() {
    return {
      user_data : '',
    }
  },
  components: {

  },
  mounted(){
    //this.getMe(),
  },
  methods:{
    getMe(e){
      console.log(axios.defaults.headers.common['Authorization'])
      axios
          .get ("/api/v1/users/me")
          .then(response => {
            console.log(response)
            this.user_data = response.data.username
          })
          .catch(error => {
            console.log(error)
          })
      
    },
  }

}
</script>
