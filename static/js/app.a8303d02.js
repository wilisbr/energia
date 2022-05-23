(function(){"use strict";var e={5554:function(e,t,o){var a=o(9242),s=o(3396),n=o(7139);const r={id:"wrapper"},i={class:"navbar is-success"},l={class:"navbar-brand"},u=(0,s._)("strong",null," C.W. Gestão de Energia Fotovoltaica",-1),c=(0,s._)("span",{"aria-hidden":"true"},null,-1),d=(0,s._)("span",{"aria-hidden":"true"},null,-1),m=(0,s._)("span",{"aria-hidden":"true"},null,-1),p=[c,d,m],h={class:"navbar-end"},g={class:"navbar-item"},f={class:"buttons"},_=(0,s.Uk)("Instalações"),v=(0,s.Uk)("Faturas"),b=(0,s.Uk)("Meu Perfil"),w=(0,s.Uk)("Log in"),y={class:"section"},k=(0,s._)("footer",{class:"footer"},[(0,s._)("p",{class:"has-text-centered"},"Copyright (c) 2021")],-1);function $(e,t,o,c,d,m){const $=(0,s.up)("router-link"),C=(0,s.up)("router-view");return(0,s.wg)(),(0,s.iD)("div",r,[(0,s._)("nav",i,[(0,s._)("div",l,[(0,s.Wm)($,{to:"/",class:"navbar-item"},{default:(0,s.w5)((()=>[u])),_:1}),(0,s._)("a",{class:"navbar-burger","aria-label":"menu","aria-expanded":"false","data-target":"navbar-menu",onClick:t[0]||(t[0]=e=>d.showMobileMenu=!d.showMobileMenu)},p)]),(0,s._)("div",h,[(0,s._)("div",{class:(0,n.C_)(["navbar-menu",{"is-active":d.showMobileMenu}]),id:"navbar-menu"},[(0,s._)("div",g,[(0,s._)("div",f,[""!=e.$store.state.access?((0,s.wg)(),(0,s.iD)(s.HY,{key:0},[(0,s.Wm)($,{to:"/clientes",class:"navbar-item"},{default:(0,s.w5)((()=>[_])),_:1}),(0,s.Wm)($,{to:"/faturas",class:"navbar-item"},{default:(0,s.w5)((()=>[v])),_:1}),(0,s.Wm)($,{to:"/my-account",class:"navbar-item"},{default:(0,s.w5)((()=>[b])),_:1})],64)):((0,s.wg)(),(0,s.j4)($,{key:1,to:"/log-in",class:"button is-light"},{default:(0,s.w5)((()=>[w])),_:1}))])])],2)])]),(0,s.wy)((0,s._)("progress",null,null,512),[[a.F8,e.$store.state.isLoading]]),(0,s._)("section",y,[(0,s.Wm)(C)]),k])}var C=o(6265),U=o.n(C),D={name:"App",data(){return{showMobileMenu:!1}},mounted(){this.$router.push("/")},beforeCreate(){this.$store.commit("initializeStore");const e=this.$store.state.access;U().defaults.headers.common.Authorization=e?"JWT "+e:"",console.log(U().defaults.headers.common.Authorization),document.title="Gestão Energia"}},F=o(89);const I=(0,F.Z)(D,[["render",$]]);var L=I,q=o(678);const x={class:"container"},z=(0,s.uE)('<div class="content is-normal has-text-justified"><p> Este sistema possbilita uma gestão <strong>eficiente</strong> para quem possui sistema de geração distribuída e trasfere o excedente para outras instalações, recebendo, em contrapartida, uma compensação financeira. O objetivo do sistema é automatizar todo o cálculo e a geração da cobrança para o seu cliente. O sistema torna tudo muito simples e rápido, de modo que você configura poucos parâmetros e faz o upload da conta de luz no formato PDF (o arquivo deverá ser baixado do site da CEMIG). Com poucos segundos você terá em mãos um documento explicando ao seu cliente o quanto ele economizou e quanto dele deverá te pagar.</p> Caso você precise fazer uma gestão completa, incluindo prospecção de clientes, relacionamento e cobrança, entre em contato para firmarmos uma paceria <strong>(gestao_fotovoltaica@aol.com).</strong> Caso você opter por fazer todo o trabalho, sinta-se livre para utilizar este sistema de forma <strong>gratuita!</strong><h2> Instruções de uso </h2><h3>1) Cadastrando as Instalações</h3><p> No menu superior, acesse a opção &quot;Instalações&quot; e cadastre cada instalação, preenchendo os campos cadastrais.</p><p>Uma das oções é o <strong>desconto</strong>, onde o usuário irá definir qual o percentual de desconto, em relação ao preço da concessionária. Ex: se a concessionária cobra R$ 1,00 por kwh, o usuário que definir 20% de desconto, estará cobrando R$ 0,80 centavos do cliente, por KWh.</p><p> Outra opção importante é o <strong> bônus </strong>, que corresponde a um desconto absoluto e incondicional que será aplicado no faturamento do seu cliente. Recomendamos deixar o campo com valor 0, inicialmente</p><h3>2) Fazendo upload das contas </h3><p> Após incluir a instalação do seu cliente, acesso a opção <strong>Faturas</strong> no menu superior, escolha a instalação desejada e faça o upload da fatura. Importante ressaltar que o sistema só vai reconhecer faturas baixadas <strong>diretamente do site da Cemig</strong>, no formato PDF. Estamos trabalhando para adicionar outras concessionárias. A próxima a ser incluída será a Enel</p><h3>3) Geração da cobrança</h3><p>Escolha uma das faturas que foram incluídas e clique na opção <strong>Faturar</strong>. Faça o download e envie para seu cliente!</p></div>',1),O=[z];function S(e,t,o,a,n,r){return(0,s.wg)(),(0,s.iD)("div",x,O)}var T={name:"HomeView",data(){return{user_data:""}},components:{},mounted(){},methods:{getMe(e){console.log(U().defaults.headers.common.Authorization),U().get("/api/v1/users/me").then((e=>{console.log(e),this.user_data=e.data.username})).catch((e=>{console.log(e)}))}}};const P=(0,F.Z)(T,[["render",S]]);var M=P;const N={class:"sign-up-page"},A=(0,s._)("h1",null," Sign up ",-1),V=(0,s._)("label",null,"Username:",-1),j=(0,s.Uk)(),H=(0,s._)("br",null,null,-1),E=(0,s._)("br",null,null,-1),R=(0,s._)("label",null,"Password:",-1),W=(0,s.Uk)(),K=(0,s._)("br",null,null,-1),J=(0,s._)("br",null,null,-1),Y=(0,s._)("label",null,"Password 2:",-1),Z=(0,s.Uk)(),G=(0,s._)("br",null,null,-1),B=(0,s._)("br",null,null,-1),Q={key:0,class:"notification is-danger"},X=(0,s._)("button",{type:"submit"}," Sign up",-1);function ee(e,t,o,r,i,l){return(0,s.wg)(),(0,s.iD)("div",N,[A,(0,s._)("form",{onSubmit:t[3]||(t[3]=(0,a.iM)(((...e)=>l.submitForm&&l.submitForm(...e)),["prevent"]))},[V,(0,s.wy)((0,s._)("input",{type:"email",name:"username","onUpdate:modelValue":t[0]||(t[0]=e=>i.username=e)},null,512),[[a.nr,i.username]]),j,H,E,R,(0,s.wy)((0,s._)("input",{type:"password",name:"password","onUpdate:modelValue":t[1]||(t[1]=e=>i.password=e)},null,512),[[a.nr,i.password]]),W,K,J,Y,(0,s.wy)((0,s._)("input",{type:"password",name:"password2","onUpdate:modelValue":t[2]||(t[2]=e=>i.password2=e)},null,512),[[a.nr,i.password2]]),Z,G,B,i.errors.length?((0,s.wg)(),(0,s.iD)("div",Q,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.errors,(e=>((0,s.wg)(),(0,s.iD)("p",{key:e},(0,n.zw)(e),1)))),128))])):(0,s.kq)("",!0),X],32)])}var te=o(5597),oe={name:"SignUp",data(){return{username:"",password:"",password2:"",errors:[]}},methods:{submitForm(e){if(this.errors=[],""===this.username&&this.errors.push("The username is missing"),""===this.password&&this.errors.push("The password is too short"),this.password!==this.password2&&this.errors.push("The passwords doesn't match"),!this.errors.length){const e={username:this.username,password:this.password};U().post("/api/v1/users/",e).then((e=>{(0,te.toast)({message:"Account created, please log in!",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.$router.push("/log-in")})).catch((e=>{if(e.response){for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);console.log(JSON.stringify(e.response.data))}else e.message&&(this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e)))}))}}}};const ae=(0,F.Z)(oe,[["render",ee]]);var se=ae;const ne={class:"log-in-page"},re=(0,s._)("h1",null," Log In ",-1),ie=(0,s._)("label",null,"Username:",-1),le=(0,s.Uk)(),ue=(0,s._)("br",null,null,-1),ce=(0,s._)("br",null,null,-1),de=(0,s._)("label",null,"Password:",-1),me=(0,s.Uk)(),pe=(0,s._)("br",null,null,-1),he=(0,s._)("br",null,null,-1),ge={key:0,class:"notification is-danger"},fe=(0,s._)("button",{type:"submit"},"Log in",-1),_e=(0,s._)("a",{href:"http://127.0.0.1:8000/accounts/password_reset/"}," Esqueci minha senha ",-1),ve=(0,s.Uk)(" Ou "),be=(0,s.Uk)("Clique aqui"),we=(0,s.Uk)(" para se cadastrar! ");function ye(e,t,o,r,i,l){const u=(0,s.up)("router-link");return(0,s.wg)(),(0,s.iD)("div",ne,[re,(0,s._)("form",{onSubmit:t[2]||(t[2]=(0,a.iM)(((...e)=>l.submitForm&&l.submitForm(...e)),["prevent"]))},[ie,(0,s.wy)((0,s._)("input",{type:"email",name:"username","onUpdate:modelValue":t[0]||(t[0]=e=>i.username=e)},null,512),[[a.nr,i.username]]),le,ue,ce,de,(0,s.wy)((0,s._)("input",{type:"password",name:"password","onUpdate:modelValue":t[1]||(t[1]=e=>i.password=e)},null,512),[[a.nr,i.password]]),me,pe,he,i.errors.length?((0,s.wg)(),(0,s.iD)("div",ge,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.errors,(e=>((0,s.wg)(),(0,s.iD)("p",{key:e},(0,n.zw)(e),1)))),128))])):(0,s.kq)("",!0),fe,_e,ve,(0,s.Wm)(u,{to:"/sign-up"},{default:(0,s.w5)((()=>[be])),_:1}),we],32)])}var ke={name:"LogIn",data(){return{username:"",password:"",errors:[]}},methods:{submitForm(e){U().defaults.headers.common.Authorization="",localStorage.removeItem("access");const t={username:this.username,password:this.password};U().post("/api/v1/jwt/create/",t).then((e=>{console.log("Deu certo!"),console.log(e);const t=e.data.access;this.$store.commit("setAccess",t),U().defaults.headers.common.Authorization="JWT "+t,localStorage.setItem("access",t),this.$router.push("/")})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))}))}}};const $e=(0,F.Z)(ke,[["render",ye]]);var Ce=$e;const Ue={class:"page-my-account"},De={class:"columns is-multiline"},Fe={class:"column is-12"},Ie=["src"],Le={class:"column is-12"},qe=(0,s._)("hr",null,null,-1);function xe(e,t,o,a,r,i){return(0,s.wg)(),(0,s.iD)("div",Ue,[(0,s._)("div",De,[(0,s._)("div",Fe,[(0,s._)("span",{src:r.user_data},(0,n.zw)(r.user_data),9,Ie)]),(0,s._)("div",Le,[(0,s._)("button",{onClick:t[0]||(t[0]=e=>i.logout()),class:"button is-danger"},"Log out")]),qe])])}var ze={name:"MyAccount",components:{},data(){return{user_data:""}},mounted(){this.getMe()},methods:{logout(){U().defaults.headers.common.Authorization="",localStorage.removeItem("access"),this.$store.commit("removeToken"),this.$router.push("/")},async getMe(e){this.$store.commit("setIsLoading",!0),console.log(U().defaults.headers.common.Authorization),await U().get("/api/v1/users/me").then((e=>{console.log(e),this.user_data=e.data.username})).catch((e=>{console.log(e)})),this.$store.commit("setIsLoading",!1)}}};const Oe=(0,F.Z)(ze,[["render",xe]]);var Se=Oe;const Te={class:"page-cart"},Pe={class:"columns is-multiline"},Me=(0,s._)("div",{class:"column is-12"},[(0,s._)("h1",{class:"title"},"Faturas")],-1),Ne={key:0,class:"notification is-danger"},Ae={class:"column is-12 box"},Ve=(0,s._)("label",null,"Instalação cliente",-1),je=["value"],He=(0,s._)("br",null,null,-1),Ee=(0,s._)("br",null,null,-1),Re=(0,s._)("button",{type:"submit"},"Inserir Fatura",-1),We=(0,s._)("br",null,null,-1),Ke=(0,s._)("hr",null,null,-1),Je={key:0,class:"table is-fullwidth"},Ye=(0,s._)("thead",null,[(0,s._)("tr",null,[(0,s._)("th",null,"Instalação"),(0,s._)("th",null,"Mês de Referência"),(0,s._)("th",null,"Ação")])],-1),Ze=["onClick"],Ge=["onClick"],Be={key:1};function Qe(e,t,o,r,i,l){return(0,s.wg)(),(0,s.iD)("div",Te,[(0,s._)("div",Pe,[Me,i.errors.length?((0,s.wg)(),(0,s.iD)("div",Ne,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.errors,(e=>((0,s.wg)(),(0,s.iD)("p",{key:e},(0,n.zw)(e),1)))),128))])):(0,s.kq)("",!0),(0,s._)("div",Ae,[(0,s._)("form",{onSubmit:t[2]||(t[2]=(0,a.iM)(((...e)=>l.nova_fatura&&l.nova_fatura(...e)),["prevent"]))},[Ve,(0,s.wy)((0,s._)("select",{required:"","onUpdate:modelValue":t[0]||(t[0]=e=>i.id_cliente=e)},[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.clientes,(e=>((0,s.wg)(),(0,s.iD)("option",{value:e.id,key:e.id},(0,n.zw)(e.nome),9,je)))),128))],512),[[a.bM,i.id_cliente]]),He,Ee,(0,s._)("input",{required:"",type:"file",id:"nova_fatura",name:"nova_fatura",accept:".pdf",onChange:t[1]||(t[1]=(...e)=>l.onFileChange&&l.onFileChange(...e))},null,32),Re],32),We,Ke,i.faturas.length>0?((0,s.wg)(),(0,s.iD)("table",Je,[Ye,(0,s._)("tbody",null,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.faturas,(t=>((0,s.wg)(),(0,s.iD)("tr",{key:t.id},[(0,s._)("td",null,(0,n.zw)(t.nome_cliente),1),(0,s._)("td",null,(0,n.zw)(t.referencia),1),(0,s._)("td",null,[(0,s._)("button",{onClick:o=>e.$router.push("/fatura/"+t.id)},"Faturar",8,Ze),(0,s._)("button",{onClick:e=>l.apagar(t)},"Remover",8,Ge)])])))),128))])])):((0,s.wg)(),(0,s.iD)("p",Be,"Não foram encontradas faturas..."))])])])}var Xe={name:"Faturas",data(){return{faturas:[],clientes:[],errors:[],fatura:Object,id_cliente:-1,conta_pdf:Object}},components:{},mounted(){this.$store.commit("setIsLoading",!0),this.getFaturamentos(),this.getClientes(),this.$store.commit("setIsLoading",!1)},methods:{logout(){(0,te.toast)({message:"Ticket expirado. Faça novo login",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),U().defaults.headers.common.Authorization="",localStorage.removeItem("access"),this.$store.commit("removeToken"),this.$router.push("/log-in")},async getClientes(){await new Promise((e=>setTimeout(e,1e3))),await U().get("/api/v1/clientes/").then((e=>{this.clientes=e.data,console.log(e)})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)}))},onFileChange(e){var t=e.target.files||e.dataTransfer.files;t.length&&(this.conta_pdf=t[0])},upload_fatura:async function(e){let t=new FormData;this.conta_pdf&&t.append("conta_pdf",this.conta_pdf),U().defaults.headers.put["Content-Type"]="application/json",await U().put(`/api/v1/faturamentos/${this.fatura.id}/`,t).then((e=>{this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))})),await this.carregarConta()},carregarConta:async function(e){console.log(this.fatura);let t=new FormData;t.append("id",this.fatura.id),await U().post("/api/v1/carregarConta",t).then((e=>{this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))}))},async nova_fatura(){console.log(this.errors.length),this.errors.length||(this.$store.commit("setIsLoading",!0),this.fatura={cpf_cliente:this.id_cliente},await U().post("/api/v1/faturamentos/",this.fatura).then((e=>{this.fatura=e.data})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),await this.upload_fatura(),await this.getFaturamentos(),this.$store.commit("setIsLoading",!1))},async apagar(e){this.$store.commit("setIsLoading",!0),await U()["delete"]("/api/v1/faturamentos/"+e.id+"/").then((e=>{this.getFaturamentos()})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1)},async getFaturamentos(){await U().get("/api/v1/faturamentos/").then((e=>{this.faturas=e.data,console.log(e)})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)}));for(let e=0;e<this.faturas.length;e+=1)await U().get("/api/v1/clientes/"+this.faturas[e].cpf_cliente+"/").then((t=>{this.faturas[e].nome_cliente=t.data.nome})).catch((e=>{console.log("Cliente não encontrado")}))}}};const et=(0,F.Z)(Xe,[["render",Qe]]);var tt=et;const ot=e=>((0,s.dD)("data-v-2b5c05c5"),e=e(),(0,s.Cn)(),e),at={class:"page-cart"},st=["href"],nt=ot((()=>(0,s._)("br",null,null,-1))),rt={className:"padding-table-columns"},it=ot((()=>(0,s._)("label",null,"Percentual de desconto sob o KWh:",-1))),lt=(0,s.Uk)(" %"),ut=ot((()=>(0,s._)("label",null,"Bônus adicional (R$):",-1))),ct=ot((()=>(0,s._)("br",null,null,-1))),dt=ot((()=>(0,s._)("br",null,null,-1))),mt=ot((()=>(0,s._)("button",{type:"submit"},"Gravar",-1))),pt=(0,s.Uk)(" ou "),ht=(0,s.Uk)("Voltar"),gt=["src"];function ft(e,t,o,r,i,l){const u=(0,s.up)("router-link");return(0,s.wg)(),(0,s.iD)("div",at,[(0,s._)("a",{href:i.fatura.conta_pdf,target:"_blank"},"Clique para ver fatura da concessionária",8,st),nt,(0,s._)("form",{onSubmit:t[2]||(t[2]=(0,a.iM)(((...e)=>l.gravar&&l.gravar(...e)),["prevent"]))},[(0,s._)("table",rt,[(0,s._)("tr",null,[(0,s._)("td",null,[it,(0,s.wy)((0,s._)("input",{required:"",type:"number",min:"0",max:"100",step:"1","onUpdate:modelValue":t[0]||(t[0]=e=>i.fatura.desconto=e)},null,512),[[a.nr,i.fatura.desconto]]),lt]),(0,s._)("td",null,[ut,(0,s.wy)((0,s._)("input",{required:"","onUpdate:modelValue":t[1]||(t[1]=e=>i.fatura.bonus=e),type:"number",min:"0",step:"0.01"},null,512),[[a.nr,i.fatura.bonus]]),ct,dt]),(0,s._)("td",null,[mt,pt,(0,s.Wm)(u,{to:"/faturas"},{default:(0,s.w5)((()=>[ht])),_:1})])])])],32),((0,s.wg)(),(0,s.iD)("iframe",{key:i.id_iFrameCobrancaPDF,src:`${i.baseURL}/api/v1/getFaturaPdf?id=${i.id}`,width:"100%",height:"700px"},null,8,gt)),(0,s._)("p",null,(0,n.zw)(i.baseURL),1)])}o(7008);var _t={name:"Fatura",data(){return{id:this.$route.params.id,fatura:Object,conta_pdf:Object,id_iFrameCobrancaPDF:Number,baseURL:String}},components:{},props:{},mounted(){this.id_iFrameCobrancaPDF=0,this.getFatura(),this.baseURL=U().defaults.baseURL},methods:{async getFatura(){await U().get("/api/v1/faturamentos/"+this.id+"/").then((e=>{this.fatura=e.data,console.log(e)})).catch((e=>{console.log(e)}))},carregarConta:async function(e){let t=new FormData;t.append("id",this.fatura.id),await U().post("/api/v1/carregarConta",t).then((e=>{this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))}))},gravar:async function(e){delete this.fatura.conta_pdf,await U().put(`/api/v1/faturamentos/${this.id}/`,this.fatura).then((e=>{console.log("Deu certo!"),console.log(e),this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))})),await this.carregarConta(),this.id_iFrameCobrancaPDF=this.id_iFrameCobrancaPDF+1}}};const vt=(0,F.Z)(_t,[["render",ft],["__scopeId","data-v-2b5c05c5"]]);var bt=vt;const wt=e=>((0,s.dD)("data-v-739917e2"),e=e(),(0,s.Cn)(),e),yt={class:"container"},kt=wt((()=>(0,s._)("h1",{class:"title"},"Instalações",-1))),$t={key:0,class:"notification is-danger"},Ct={class:"table"},Ut=wt((()=>(0,s._)("thead",null,[(0,s._)("tr",null,[(0,s._)("th",null,"Nome da instalação"),(0,s._)("th",null,"Endereço da Instalação"),(0,s._)("th")])],-1))),Dt=["onClick"],Ft=["onClick"];function It(e,t,o,a,r,i){return(0,s.wg)(),(0,s.iD)("div",yt,[(0,s._)("div",null,[kt,r.errors.length?((0,s.wg)(),(0,s.iD)("div",$t,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(r.errors,(e=>((0,s.wg)(),(0,s.iD)("p",{key:e},(0,n.zw)(e),1)))),128))])):(0,s.kq)("",!0),(0,s._)("button",{onClick:t[0]||(t[0]=t=>e.$router.push("/cliente/0"))},"Nova Instalação"),(0,s._)("table",Ct,[Ut,(0,s._)("tbody",null,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(r.clientes,(t=>((0,s.wg)(),(0,s.iD)("tr",{key:t.id},[(0,s._)("td",null,(0,n.zw)(t.nome),1),(0,s._)("td",null,(0,n.zw)(t.endereco),1),(0,s._)("td",null,[(0,s._)("button",{onClick:e=>i.apagar(t)},"Remover",8,Dt),(0,s._)("button",{onClick:o=>e.$router.push("/cliente/"+t.id)},"Editar",8,Ft)])])))),128))])])])])}var Lt={name:"Clientes",data(){return{clientes:[],cliente:Object,errors:[],novo_cliente:{cpf_cliente:Number,nome:"",telefone:"",endereco:"",email:"",desconto:20,bonus:0}}},components:{},mounted(){this.getClientes()},methods:{logout(){(0,te.toast)({message:"Ticket expirado. Faça novo login",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),U().defaults.headers.common.Authorization="",localStorage.removeItem("access"),this.$store.commit("removeToken"),this.$router.push("/log-in")},async apagar(e){this.$store.commit("setIsLoading",!0),console.log(e),await U()["delete"]("/api/v1/clientes/"+e.id+"/",e).then((e=>{(0,te.toast)({message:"Instalação removida",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.getClientes()})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),await new Promise((e=>setTimeout(e,3e3))),this.$store.commit("setIsLoading",!1)},async getClientes(){this.$store.commit("setIsLoading",!0),await U().get("/api/v1/clientes/").then((e=>{this.clientes=e.data,console.log(e)})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1)}}};const qt=(0,F.Z)(Lt,[["render",It],["__scopeId","data-v-739917e2"]]);var xt=qt;const zt=e=>((0,s.dD)("data-v-491eb76a"),e=e(),(0,s.Cn)(),e),Ot={class:"container"},St={key:0,class:"notification is-danger"},Tt={class:"table"},Pt=zt((()=>(0,s._)("td",null,"CPF do Cliente",-1))),Mt=(0,s.Uk)(),Nt=zt((()=>(0,s._)("td",null,"Nome da Instalação",-1))),At=(0,s.Uk)(),Vt=zt((()=>(0,s._)("td",null,"Endereço",-1))),jt=(0,s.Uk)(),Ht=zt((()=>(0,s._)("td",null,"E-mail",-1))),Et=(0,s.Uk)(),Rt=zt((()=>(0,s._)("td",null,"Telefone",-1))),Wt=(0,s.Uk)(),Kt=zt((()=>(0,s._)("td",null,"Desconto",-1))),Jt=(0,s.Uk)(),Yt=(0,s.Uk)("%"),Zt=zt((()=>(0,s._)("td",null,"Bônus",-1))),Gt=(0,s.Uk)(),Bt=(0,s.Uk)(" R$ "),Qt=zt((()=>(0,s._)("button",{type:"submit"},"Gravar",-1)));function Xt(e,t,o,r,i,l){return(0,s.wg)(),(0,s.iD)("div",Ot,[i.errors.length?((0,s.wg)(),(0,s.iD)("div",St,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.errors,(e=>((0,s.wg)(),(0,s.iD)("p",{key:e},(0,n.zw)(e),1)))),128))])):(0,s.kq)("",!0),(0,s._)("form",{onSubmit:t[8]||(t[8]=(0,a.iM)(((...e)=>l.gravar_ou_criar&&l.gravar_ou_criar(...e)),["prevent"]))},[(0,s._)("table",Tt,[(0,s._)("tbody",null,[(0,s._)("tr",null,[Pt,Mt,(0,s._)("td",null,[(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[0]||(t[0]=e=>i.cliente.cpf_cliente=e),required:"",type:"number",max:"99999999999",style:{width:"11em"},size:"11"},null,512),[[a.nr,i.cliente.cpf_cliente]])])]),(0,s._)("tr",null,[Nt,At,(0,s._)("td",null,[(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[1]||(t[1]=e=>i.cliente.nome=e),required:"",type:"text",max:"40"},null,512),[[a.nr,i.cliente.nome]])])]),(0,s._)("tr",null,[Vt,jt,(0,s._)("td",null,[(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[2]||(t[2]=e=>i.cliente.endereco=e),type:"text",max:"84"},null,512),[[a.nr,i.cliente.endereco]])])]),(0,s._)("tr",null,[Ht,Et,(0,s._)("td",null,[(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[3]||(t[3]=e=>i.cliente.email=e),type:"email"},null,512),[[a.nr,i.cliente.email]])])]),(0,s._)("tr",null,[Rt,Wt,(0,s._)("td",null,[(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[4]||(t[4]=e=>i.cliente.telefone=e),type:"text",size:"13",max:"15"},null,512),[[a.nr,i.cliente.telefone]])])]),(0,s._)("tr",null,[Kt,Jt,(0,s._)("td",null,[(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[5]||(t[5]=e=>i.cliente.desconto=e),required:"",type:"number",min:"0",max:"100",step:"1",size:"3"},null,512),[[a.nr,i.cliente.desconto]]),Yt])]),(0,s._)("tr",null,[Zt,Gt,(0,s._)("td",null,[Bt,(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[6]||(t[6]=e=>i.cliente.bonus=e),required:"",type:"number",min:"0",step:"0.01"},null,512),[[a.nr,i.cliente.bonus]])])])])]),(0,s._)("button",{onClick:t[7]||(t[7]=t=>e.$router.push("/clientes"))},"Voltar"),Qt],32)])}var eo={name:"Clientes",data(){return{cliente:{},errors:[],id:this.$route.params.id}},components:{},mounted(){0!=this.id&&(this.cliente=this.getCliente())},methods:{logout(){(0,te.toast)({message:"Ticket expirado. Faça novo login",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),U().defaults.headers.common.Authorization="",localStorage.removeItem("access"),this.$store.commit("removeToken"),this.$router.push("/log-in")},async getCliente(){this.$store.commit("setIsLoading",!0),await U().get("/api/v1/clientes/"+this.id+"/").then((e=>{this.cliente=e.data})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1)},gravar_ou_criar(){0==this.id?this.novo():this.gravar()},async gravar(){this.errors.length||(this.$store.commit("setIsLoading",!0),console.log(this.cliente),await U().put("/api/v1/clientes/"+this.id+"/",this.cliente).then((e=>{(0,te.toast)({message:"Cliente alterado",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.cliente=e.data,this.$router.push("/clientes")})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1))},async novo(){this.errors.length||(this.$store.commit("setIsLoading",!0),console.log(this.cliente),await U().post("/api/v1/clientes/",this.cliente).then((e=>{(0,te.toast)({message:"Cliente adicionado",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.cliente=e.data,this.$router.push("/clientes")})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1))}}};const to=(0,F.Z)(eo,[["render",Xt],["__scopeId","data-v-491eb76a"]]);var oo=to,ao=o(65),so=(0,ao.MT)({state:{access:"",refresh:"",isLoading:!1},mutations:{initializeStore(e){localStorage.getItem("access")?e.access=localStorage.getItem("access"):e.access=""},setAccess(e,t){e.access=t},setIsLoading(e,t){e.isLoading=t},removeToken(e){e.access=""}},actions:{},modules:{}});const no=[{path:"/",name:"home",component:M},{path:"/sign-up",name:"SignUp",component:se},{path:"/log-in",name:"LogIn",component:Ce},{path:"/my-account",name:"MyAccount",component:Se,meta:{requireLogin:!0}},{path:"/clientes",name:"Clientes",component:xt,meta:{requireLogin:!0}},{path:"/faturas",name:"Faturas",component:tt,meta:{requireLogin:!0}},{path:"/fatura/:id",name:"Fatura",component:bt,meta:{requireLogin:!0}},{path:"/cliente/:id",name:"Cliente",component:oo,meta:{requireLogin:!0}}],ro=(0,q.p7)({history:(0,q.PO)("/static/"),routes:no});ro.beforeEach(((e,t,o)=>{e.matched.some((e=>e.meta.requireLogin))&&!so.state.access?o({name:"LogIn",query:{to:e.path}}):o()}));var io=ro;U().defaults.baseURL=window.location.origin,"http://localhost:8080"==U().defaults.baseURL&&(U().defaults.baseURL="http://127.0.0.1:8000"),(0,a.ri)(L).use(so).use(io,U()).mount("#app")}},t={};function o(a){var s=t[a];if(void 0!==s)return s.exports;var n=t[a]={exports:{}};return e[a].call(n.exports,n,n.exports,o),n.exports}o.m=e,function(){var e=[];o.O=function(t,a,s,n){if(!a){var r=1/0;for(c=0;c<e.length;c++){a=e[c][0],s=e[c][1],n=e[c][2];for(var i=!0,l=0;l<a.length;l++)(!1&n||r>=n)&&Object.keys(o.O).every((function(e){return o.O[e](a[l])}))?a.splice(l--,1):(i=!1,n<r&&(r=n));if(i){e.splice(c--,1);var u=s();void 0!==u&&(t=u)}}return t}n=n||0;for(var c=e.length;c>0&&e[c-1][2]>n;c--)e[c]=e[c-1];e[c]=[a,s,n]}}(),function(){o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,{a:t}),t}}(),function(){o.d=function(e,t){for(var a in t)o.o(t,a)&&!o.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:t[a]})}}(),function(){o.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={143:0};o.O.j=function(t){return 0===e[t]};var t=function(t,a){var s,n,r=a[0],i=a[1],l=a[2],u=0;if(r.some((function(t){return 0!==e[t]}))){for(s in i)o.o(i,s)&&(o.m[s]=i[s]);if(l)var c=l(o)}for(t&&t(a);u<r.length;u++)n=r[u],o.o(e,n)&&e[n]&&e[n][0](),e[n]=0;return o.O(c)},a=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];a.forEach(t.bind(null,0)),a.push=t.bind(null,a.push.bind(a))}();var a=o.O(void 0,[998],(function(){return o(5554)}));a=o.O(a)})();
//# sourceMappingURL=app.a8303d02.js.map