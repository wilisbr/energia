(function(){"use strict";var e={8123:function(e,t,o){var a=o(9242),n=o(3396),s=o(7139);const r={id:"wrapper"},i={class:"navbar is-success"},l={class:"navbar-brand"},u=(0,n._)("strong",null," C.W. Gestão de Energia Fotovoltaica",-1),c=(0,n._)("span",{"aria-hidden":"true"},null,-1),d=(0,n._)("span",{"aria-hidden":"true"},null,-1),m=(0,n._)("span",{"aria-hidden":"true"},null,-1),p=[c,d,m],h={class:"navbar-end"},g={class:"navbar-item"},f={class:"buttons"},_=(0,n.Uk)("Instalações"),v=(0,n.Uk)("Faturas"),w=(0,n.Uk)("Meu Perfil"),b=(0,n.Uk)("Log in"),y={class:"section"},k=(0,n._)("footer",{class:"footer"},[(0,n._)("p",{class:"has-text-centered"},"Copyright (c) 2021")],-1);function U(e,t,o,c,d,m){const U=(0,n.up)("router-link"),C=(0,n.up)("router-view");return(0,n.wg)(),(0,n.iD)("div",r,[(0,n._)("nav",i,[(0,n._)("div",l,[(0,n.Wm)(U,{to:"/",class:"navbar-item"},{default:(0,n.w5)((()=>[u])),_:1}),(0,n._)("a",{class:"navbar-burger","aria-label":"menu","aria-expanded":"false","data-target":"navbar-menu",onClick:t[0]||(t[0]=e=>d.showMobileMenu=!d.showMobileMenu)},p)]),(0,n._)("div",h,[(0,n._)("div",{class:(0,s.C_)(["navbar-menu",{"is-active":d.showMobileMenu}]),id:"navbar-menu"},[(0,n._)("div",g,[(0,n._)("div",f,[""!=e.$store.state.access?((0,n.wg)(),(0,n.iD)(n.HY,{key:0},[(0,n.Wm)(U,{to:"/clientes",class:"navbar-item"},{default:(0,n.w5)((()=>[_])),_:1}),(0,n.Wm)(U,{to:"/faturas",class:"navbar-item"},{default:(0,n.w5)((()=>[v])),_:1}),(0,n.Wm)(U,{to:"/my-account",class:"navbar-item"},{default:(0,n.w5)((()=>[w])),_:1})],64)):((0,n.wg)(),(0,n.j4)(U,{key:1,to:"/log-in",class:"button is-light"},{default:(0,n.w5)((()=>[b])),_:1}))])])],2)])]),(0,n.wy)((0,n._)("progress",null,null,512),[[a.F8,e.$store.state.isLoading]]),(0,n._)("section",y,[(0,n.Wm)(C)]),k])}var C=o(6265),$=o.n(C),F={name:"App",data(){return{showMobileMenu:!1}},mounted(){},beforeCreate(){this.$store.commit("initializeStore");const e=this.$store.state.access;$().defaults.headers.common.Authorization=e?"JWT "+e:"",console.log($().defaults.headers.common.Authorization),document.title="Gestão Energia"}},x=o(89);const D=(0,x.Z)(F,[["render",U]]);var I=D,L=o(678);const O={class:"container"},q=(0,n.uE)('<div class="content is-normal has-text-justified"><p> Este sistema possbilita uma gestão <strong>eficiente</strong> para quem possui sistema de geração distribuída e trasfere o excedente para outras instalações, recebendo, em contrapartida, uma compensação financeira. O objetivo do sistema é automatizar todo o cálculo e a geração da cobrança para o seu cliente. O sistema torna tudo muito simples e rápido, de modo que você configura poucos parâmetros e faz o upload da conta de luz no formato PDF (o arquivo deverá ser baixado do site da CEMIG). Com poucos segundos você terá em mãos um documento explicando ao seu cliente o quanto ele economizou e quanto dele deverá te pagar.</p> Caso você precise fazer uma gestão completa, incluindo prospecção de clientes, relacionamento e cobrança, entre em contato para firmarmos uma paceria <strong>(gestao_fotovoltaica@aol.com).</strong> Caso você opter por fazer todo o trabalho, sinta-se livre para utilizar este sistema de forma <strong>gratuita!</strong><h2> Instruções de uso </h2><h3>1) Cadastrando as Instalações</h3><p> No menu superior, acesse a opção &quot;Instalações&quot; e cadastre cada instalação, preenchendo os campos cadastrais.</p><p>Uma das oções é o <strong>desconto</strong>, onde o usuário irá definir qual o percentual de desconto, em relação ao preço da concessionária. Ex: se a concessionária cobra R$ 1,00 por kwh, o usuário que definir 20% de desconto, estará cobrando R$ 0,80 centavos do cliente, por KWh.</p><p> Outra opção importante é o <strong> bônus </strong>, que corresponde a um desconto absoluto e incondicional que será aplicado no faturamento do seu cliente. Recomendamos deixar o campo com valor 0, inicialmente</p><h3>2) Fazendo upload das contas </h3><p> Após incluir a instalação do seu cliente, acesso a opção <strong>Faturas</strong> no menu superior, escolha a instalação desejada e faça o upload da fatura. Importante ressaltar que o sistema só vai reconhecer faturas baixadas <strong>diretamente do site da Cemig</strong>, no formato PDF. Estamos trabalhando para adicionar outras concessionárias. A próxima a ser incluída será a Enel</p><h3>3) Geração da cobrança</h3><p>Escolha uma das faturas que foram incluídas e clique na opção <strong>Faturar</strong>. Faça o download e envie para seu cliente!</p></div>',1),z=[q];function S(e,t,o,a,s,r){return(0,n.wg)(),(0,n.iD)("div",O,z)}var V={name:"HomeView",data(){return{user_data:""}},components:{},mounted(){},methods:{getMe(e){console.log($().defaults.headers.common.Authorization),$().get("/api/v1/users/me").then((e=>{console.log(e),this.user_data=e.data.username})).catch((e=>{console.log(e)}))}}};const P=(0,x.Z)(V,[["render",S]]);var T=P;const M={class:"sign-up-page"},N=(0,n._)("h1",null," Sign up ",-1),A=(0,n._)("label",null,"Username:",-1),R=(0,n.Uk)(),j=(0,n._)("br",null,null,-1),H=(0,n._)("br",null,null,-1),E=(0,n._)("label",null,"Password:",-1),W=(0,n.Uk)(),J=(0,n._)("br",null,null,-1),K=(0,n._)("br",null,null,-1),Y=(0,n._)("label",null,"Password 2:",-1),Z=(0,n.Uk)(),G=(0,n._)("br",null,null,-1),B=(0,n._)("br",null,null,-1),Q={key:0,class:"notification is-danger"},X=(0,n._)("button",{type:"submit"}," Sign up",-1);function ee(e,t,o,r,i,l){return(0,n.wg)(),(0,n.iD)("div",M,[N,(0,n._)("form",{onSubmit:t[3]||(t[3]=(0,a.iM)(((...e)=>l.submitForm&&l.submitForm(...e)),["prevent"]))},[A,(0,n.wy)((0,n._)("input",{type:"email",name:"username","onUpdate:modelValue":t[0]||(t[0]=e=>i.username=e)},null,512),[[a.nr,i.username]]),R,j,H,E,(0,n.wy)((0,n._)("input",{type:"password",name:"password","onUpdate:modelValue":t[1]||(t[1]=e=>i.password=e)},null,512),[[a.nr,i.password]]),W,J,K,Y,(0,n.wy)((0,n._)("input",{type:"password",name:"password2","onUpdate:modelValue":t[2]||(t[2]=e=>i.password2=e)},null,512),[[a.nr,i.password2]]),Z,G,B,i.errors.length?((0,n.wg)(),(0,n.iD)("div",Q,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(i.errors,(e=>((0,n.wg)(),(0,n.iD)("p",{key:e},(0,s.zw)(e),1)))),128))])):(0,n.kq)("",!0),X],32)])}var te=o(5597),oe={name:"SignUp",data(){return{username:"",password:"",password2:"",errors:[]}},methods:{submitForm(e){if(this.errors=[],""===this.username&&this.errors.push("The username is missing"),""===this.password&&this.errors.push("The password is too short"),this.password!==this.password2&&this.errors.push("The passwords doesn't match"),!this.errors.length){const e={username:this.username,password:this.password};$().post("/api/v1/users/",e).then((e=>{(0,te.toast)({message:"Account created, please log in!",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.$router.push("/log-in")})).catch((e=>{if(e.response){for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);console.log(JSON.stringify(e.response.data))}else e.message&&(this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e)))}))}}}};const ae=(0,x.Z)(oe,[["render",ee]]);var ne=ae;const se={class:"log-in-page"},re=(0,n._)("h1",null," Log In ",-1),ie=(0,n._)("label",null,"Username:",-1),le=(0,n.Uk)(),ue=(0,n._)("br",null,null,-1),ce=(0,n._)("br",null,null,-1),de=(0,n._)("label",null,"Password:",-1),me=(0,n.Uk)(),pe=(0,n._)("br",null,null,-1),he=(0,n._)("br",null,null,-1),ge={key:0,class:"notification is-danger"},fe=(0,n._)("button",{type:"submit"},"Log in",-1),_e=(0,n._)("a",{href:"http://127.0.0.1:8000/accounts/password_reset/"}," Esqueci minha senha ",-1),ve=(0,n.Uk)(" Ou "),we=(0,n.Uk)("Clique aqui"),be=(0,n.Uk)(" para se cadastrar! ");function ye(e,t,o,r,i,l){const u=(0,n.up)("router-link");return(0,n.wg)(),(0,n.iD)("div",se,[re,(0,n._)("form",{onSubmit:t[2]||(t[2]=(0,a.iM)(((...e)=>l.submitForm&&l.submitForm(...e)),["prevent"]))},[ie,(0,n.wy)((0,n._)("input",{type:"email",name:"username","onUpdate:modelValue":t[0]||(t[0]=e=>i.username=e)},null,512),[[a.nr,i.username]]),le,ue,ce,de,(0,n.wy)((0,n._)("input",{type:"password",name:"password","onUpdate:modelValue":t[1]||(t[1]=e=>i.password=e)},null,512),[[a.nr,i.password]]),me,pe,he,i.errors.length?((0,n.wg)(),(0,n.iD)("div",ge,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(i.errors,(e=>((0,n.wg)(),(0,n.iD)("p",{key:e},(0,s.zw)(e),1)))),128))])):(0,n.kq)("",!0),fe,_e,ve,(0,n.Wm)(u,{to:"/sign-up"},{default:(0,n.w5)((()=>[we])),_:1}),be],32)])}var ke={name:"LogIn",data(){return{username:"",password:"",errors:[]}},methods:{submitForm(e){$().defaults.headers.common.Authorization="",localStorage.removeItem("access");const t={username:this.username,password:this.password};$().post("/api/v1/jwt/create/",t).then((e=>{console.log("Deu certo!"),console.log(e);const t=e.data.access;this.$store.commit("setAccess",t),$().defaults.headers.common.Authorization="JWT "+t,localStorage.setItem("access",t),this.$router.push("/")})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))}))}}};const Ue=(0,x.Z)(ke,[["render",ye]]);var Ce=Ue;const $e={class:"page-my-account"},Fe={class:"columns is-multiline"},xe={class:"column is-12"},De=["src"],Ie={class:"column is-12"},Le=(0,n._)("hr",null,null,-1);function Oe(e,t,o,a,r,i){return(0,n.wg)(),(0,n.iD)("div",$e,[(0,n._)("div",Fe,[(0,n._)("div",xe,[(0,n._)("span",{src:r.user_data},(0,s.zw)(r.user_data),9,De)]),(0,n._)("div",Ie,[(0,n._)("button",{onClick:t[0]||(t[0]=e=>i.logout()),class:"button is-danger"},"Log out")]),Le])])}var qe={name:"MyAccount",components:{},data(){return{user_data:""}},mounted(){this.getMe()},methods:{logout(){$().defaults.headers.common.Authorization="",localStorage.removeItem("access"),this.$store.commit("removeToken"),this.$router.push("/")},async getMe(e){this.$store.commit("setIsLoading",!0),console.log($().defaults.headers.common.Authorization),await $().get("/api/v1/users/me").then((e=>{console.log(e),this.user_data=e.data.username})).catch((e=>{console.log(e)})),this.$store.commit("setIsLoading",!1)}}};const ze=(0,x.Z)(qe,[["render",Oe]]);var Se=ze;const Ve={class:"page-cart"},Pe={class:"columns is-multiline"},Te=(0,n._)("div",{class:"column is-12"},[(0,n._)("h1",{class:"title"},"Faturas")],-1),Me={key:0,class:"notification is-danger"},Ne={class:"column is-12 box"},Ae=(0,n._)("label",null,"Instalação cliente",-1),Re=["value"],je=(0,n._)("br",null,null,-1),He=(0,n._)("br",null,null,-1),Ee=(0,n._)("button",{type:"submit"},"Inserir Fatura",-1),We=(0,n._)("br",null,null,-1),Je=(0,n._)("hr",null,null,-1),Ke={key:0,class:"table is-fullwidth"},Ye=(0,n._)("thead",null,[(0,n._)("tr",null,[(0,n._)("th",null,"Instalação"),(0,n._)("th",null,"Mês de Referência"),(0,n._)("th",null,"Ação")])],-1),Ze=["onClick"],Ge=["onClick"],Be={key:1};function Qe(e,t,o,r,i,l){return(0,n.wg)(),(0,n.iD)("div",Ve,[(0,n._)("div",Pe,[Te,i.errors.length?((0,n.wg)(),(0,n.iD)("div",Me,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(i.errors,(e=>((0,n.wg)(),(0,n.iD)("p",{key:e},(0,s.zw)(e),1)))),128))])):(0,n.kq)("",!0),(0,n._)("div",Ne,[(0,n._)("form",{onSubmit:t[2]||(t[2]=(0,a.iM)(((...e)=>l.nova_fatura&&l.nova_fatura(...e)),["prevent"]))},[Ae,(0,n.wy)((0,n._)("select",{required:"","onUpdate:modelValue":t[0]||(t[0]=e=>i.id_cliente=e)},[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(i.clientes,(e=>((0,n.wg)(),(0,n.iD)("option",{value:e.id,key:e.id},(0,s.zw)(e.nome),9,Re)))),128))],512),[[a.bM,i.id_cliente]]),je,He,(0,n._)("input",{required:"",type:"file",id:"nova_fatura",name:"nova_fatura",accept:".pdf",onChange:t[1]||(t[1]=(...e)=>l.onFileChange&&l.onFileChange(...e))},null,32),Ee],32),We,Je,i.faturas.length>0?((0,n.wg)(),(0,n.iD)("table",Ke,[Ye,(0,n._)("tbody",null,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(i.faturas,(t=>((0,n.wg)(),(0,n.iD)("tr",{key:t.id},[(0,n._)("td",null,(0,s.zw)(t.nome_cliente),1),(0,n._)("td",null,(0,s.zw)(t.referencia),1),(0,n._)("td",null,[(0,n._)("button",{onClick:o=>e.$router.push("/fatura/"+t.id)},"Faturar",8,Ze),(0,n._)("button",{onClick:e=>l.apagar(t)},"Remover",8,Ge)])])))),128))])])):((0,n.wg)(),(0,n.iD)("p",Be,"Não foram encontradas faturas..."))])])])}var Xe={name:"Faturas",data(){return{faturas:[],clientes:[],errors:[],fatura:Object,id_cliente:-1,conta_pdf:Object}},components:{},mounted(){this.$store.commit("setIsLoading",!0),this.getFaturamentos(),this.getClientes(),this.$store.commit("setIsLoading",!1)},methods:{logout(){(0,te.toast)({message:"Ticket expirado. Faça novo login",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),$().defaults.headers.common.Authorization="",localStorage.removeItem("access"),this.$store.commit("removeToken"),this.$router.push("/log-in")},async getClientes(){await new Promise((e=>setTimeout(e,1e3))),await $().get("/api/v1/clientes/").then((e=>{this.clientes=e.data,console.log(e)})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)}))},onFileChange(e){var t=e.target.files||e.dataTransfer.files;t.length&&(this.conta_pdf=t[0])},upload_fatura:async function(e){let t=new FormData;this.conta_pdf&&t.append("conta_pdf",this.conta_pdf),$().defaults.headers.put["Content-Type"]="application/json",await $().put(`/api/v1/faturamentos/${this.fatura.id}/`,t).then((e=>{this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))})),await this.carregarConta()},carregarConta:async function(e){console.log(this.fatura);let t=new FormData;t.append("id",this.fatura.id),await $().post("/api/v1/carregarConta",t).then((e=>{this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))}))},async nova_fatura(){console.log(this.errors.length),this.errors.length||(this.$store.commit("setIsLoading",!0),this.fatura={cpf_cliente:this.id_cliente},await $().post("/api/v1/faturamentos/",this.fatura).then((e=>{this.fatura=e.data})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),await this.upload_fatura(),await this.getFaturamentos(),this.$store.commit("setIsLoading",!1))},async apagar(e){this.$store.commit("setIsLoading",!0),await $()["delete"]("/api/v1/faturamentos/"+e.id+"/").then((e=>{this.getFaturamentos()})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1)},async getFaturamentos(){await $().get("/api/v1/faturamentos/").then((e=>{this.faturas=e.data,console.log(e)})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)}));for(let e=0;e<this.faturas.length;e+=1)await $().get("/api/v1/clientes/"+this.faturas[e].cpf_cliente+"/").then((t=>{this.faturas[e].nome_cliente=t.data.nome})).catch((e=>{console.log("Cliente não encontrado")}))}}};const et=(0,x.Z)(Xe,[["render",Qe]]);var tt=et;const ot=e=>((0,n.dD)("data-v-2b5c05c5"),e=e(),(0,n.Cn)(),e),at={class:"page-cart"},nt=["href"],st=ot((()=>(0,n._)("br",null,null,-1))),rt={className:"padding-table-columns"},it=ot((()=>(0,n._)("label",null,"Percentual de desconto sob o KWh:",-1))),lt=(0,n.Uk)(" %"),ut=ot((()=>(0,n._)("label",null,"Bônus adicional (R$):",-1))),ct=ot((()=>(0,n._)("br",null,null,-1))),dt=ot((()=>(0,n._)("br",null,null,-1))),mt=ot((()=>(0,n._)("button",{type:"submit"},"Gravar",-1))),pt=(0,n.Uk)(" ou "),ht=(0,n.Uk)("Voltar"),gt=["src"];function ft(e,t,o,r,i,l){const u=(0,n.up)("router-link");return(0,n.wg)(),(0,n.iD)("div",at,[(0,n._)("a",{href:i.fatura.conta_pdf,target:"_blank"},"Clique para ver fatura da concessionária",8,nt),st,(0,n._)("form",{onSubmit:t[2]||(t[2]=(0,a.iM)(((...e)=>l.gravar&&l.gravar(...e)),["prevent"]))},[(0,n._)("table",rt,[(0,n._)("tr",null,[(0,n._)("td",null,[it,(0,n.wy)((0,n._)("input",{required:"",type:"number",min:"0",max:"100",step:"1","onUpdate:modelValue":t[0]||(t[0]=e=>i.fatura.desconto=e)},null,512),[[a.nr,i.fatura.desconto]]),lt]),(0,n._)("td",null,[ut,(0,n.wy)((0,n._)("input",{required:"","onUpdate:modelValue":t[1]||(t[1]=e=>i.fatura.bonus=e),type:"number",min:"0",step:"0.01"},null,512),[[a.nr,i.fatura.bonus]]),ct,dt]),(0,n._)("td",null,[mt,pt,(0,n.Wm)(u,{to:"/faturas"},{default:(0,n.w5)((()=>[ht])),_:1})])])])],32),((0,n.wg)(),(0,n.iD)("iframe",{key:i.id_iFrameCobrancaPDF,src:`${i.baseURL}/api/v1/getFaturaPdf?id=${i.id}`,width:"100%",height:"700px"},null,8,gt)),(0,n._)("p",null,(0,s.zw)(i.baseURL),1)])}o(7008);var _t={name:"Fatura",data(){return{id:this.$route.params.id,fatura:Object,conta_pdf:Object,id_iFrameCobrancaPDF:Number,baseURL:String}},components:{},props:{},mounted(){this.id_iFrameCobrancaPDF=0,this.getFatura(),this.baseURL=$().defaults.baseURL},methods:{async getFatura(){await $().get("/api/v1/faturamentos/"+this.id+"/").then((e=>{this.fatura=e.data,console.log(e)})).catch((e=>{console.log(e)}))},carregarConta:async function(e){let t=new FormData;t.append("id",this.fatura.id),await $().post("/api/v1/carregarConta",t).then((e=>{this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))}))},gravar:async function(e){delete this.fatura.conta_pdf,await $().put(`/api/v1/faturamentos/${this.id}/`,this.fatura).then((e=>{console.log("Deu certo!"),console.log(e),this.fatura=e.data})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))})),await this.carregarConta(),this.id_iFrameCobrancaPDF=this.id_iFrameCobrancaPDF+1}}};const vt=(0,x.Z)(_t,[["render",ft],["__scopeId","data-v-2b5c05c5"]]);var wt=vt;const bt=e=>((0,n.dD)("data-v-584dc5f7"),e=e(),(0,n.Cn)(),e),yt={class:"page-cart"},kt={class:"columns is-multiline"},Ut=bt((()=>(0,n._)("div",{class:"column is-12"},[(0,n._)("h1",{class:"title"},"Instalações clientes")],-1))),Ct={class:"column is-12 box"},$t={key:0,class:"notification is-danger"},Ft={class:"table is-fullwidth"},xt=bt((()=>(0,n._)("thead",null,[(0,n._)("tr",null,[(0,n._)("th",null,"CPF do Cliente"),(0,n._)("th",null,"Nome da instalação"),(0,n._)("th",null,"Endereço da Instalação"),(0,n._)("th",null,"E-mail"),(0,n._)("th",null,"Telefone"),(0,n._)("th",null,"Desconto"),(0,n._)("th",null,"Bônus"),(0,n._)("th")])],-1))),Dt=["onUpdate:modelValue"],It=["onUpdate:modelValue"],Lt=["onUpdate:modelValue"],Ot=["onUpdate:modelValue"],qt=["onUpdate:modelValue"],zt=["onUpdate:modelValue"],St=(0,n.Uk)("%"),Vt=(0,n.Uk)(" R$ "),Pt=["onUpdate:modelValue"],Tt=["onClick"],Mt=["onClick"],Nt=(0,n.Uk)("%"),At=(0,n.Uk)("R$");function Rt(e,t,o,r,i,l){return(0,n.wg)(),(0,n.iD)("div",yt,[(0,n._)("div",kt,[Ut,(0,n._)("div",Ct,[i.errors.length?((0,n.wg)(),(0,n.iD)("div",$t,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(i.errors,(e=>((0,n.wg)(),(0,n.iD)("p",{key:e},(0,s.zw)(e),1)))),128))])):(0,n.kq)("",!0),(0,n._)("table",Ft,[xt,(0,n._)("tbody",null,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(i.clientes,(e=>((0,n.wg)(),(0,n.iD)("tr",{key:e.id},[(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t=>e.cpf_cliente=t,type:"number",max:"99999999999",style:{width:"11em"},size:"11"},null,8,Dt),[[a.nr,e.cpf_cliente]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t=>e.nome=t,type:"text",max:"40"},null,8,It),[[a.nr,e.nome]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t=>e.endereco=t,type:"text",max:"84"},null,8,Lt),[[a.nr,e.endereco]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t=>e.email=t,type:"email"},null,8,Ot),[[a.nr,e.email]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t=>e.telefone=t,type:"text",size:"13",max:"15"},null,8,qt),[[a.nr,e.telefone]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t=>e.desconto=t,type:"number",min:"0",max:"100",step:"1",size:"3"},null,8,zt),[[a.nr,e.desconto]]),St]),(0,n._)("td",null,[Vt,(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t=>e.bonus=t,type:"number",min:"0",step:"0.01"},null,8,Pt),[[a.nr,e.bonus]])]),(0,n._)("td",null,[(0,n._)("button",{onClick:t=>l.gravar(e)},"Gravar",8,Tt),(0,n._)("button",{onClick:t=>l.apagar(e)},"Remover",8,Mt)])])))),128)),(0,n._)("tr",null,[(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[0]||(t[0]=e=>i.novo_cliente.cpf_cliente=e),type:"number",max:"99999999999",style:{width:"11em"},size:"11"},null,512),[[a.nr,i.novo_cliente.cpf_cliente]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[1]||(t[1]=e=>i.novo_cliente.nome=e),type:"text",max:"40"},null,512),[[a.nr,i.novo_cliente.nome]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[2]||(t[2]=e=>i.novo_cliente.endereco=e),type:"text",max:"84"},null,512),[[a.nr,i.novo_cliente.endereco]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[3]||(t[3]=e=>i.novo_cliente.email=e),type:"email"},null,512),[[a.nr,i.novo_cliente.email]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[4]||(t[4]=e=>i.novo_cliente.telefone=e),type:"text",size:"13",max:"15"},null,512),[[a.nr,i.novo_cliente.telefone]])]),(0,n._)("td",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[5]||(t[5]=e=>i.novo_cliente.desconto=e),type:"number",min:"0",max:"100",step:"1",size:"3"},null,512),[[a.nr,i.novo_cliente.desconto]]),Nt]),(0,n._)("td",null,[At,(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[6]||(t[6]=e=>i.novo_cliente.bonus=e),type:"number",min:"0",step:"0.01"},null,512),[[a.nr,i.novo_cliente.bonus]])]),(0,n._)("td",null,[(0,n._)("button",{onClick:t[7]||(t[7]=e=>l.novo(i.novo_cliente))},"Incluir")])])])])])])])}var jt={name:"Clientes",data(){return{clientes:[],cliente:Number,errors:[],novo_cliente:{cpf_cliente:Number,nome:"",telefone:"",endereco:"",email:"",desconto:20,bonus:0}}},components:{},mounted(){this.getClientes()},methods:{logout(){(0,te.toast)({message:"Ticket expirado. Faça novo login",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),$().defaults.headers.common.Authorization="",localStorage.removeItem("access"),this.$store.commit("removeToken"),this.$router.push("/log-in")},async validar_campos(e){if(this.errors=[],0==/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(e.email))return this.errors.push("Preencha o e-mail corretamente"),null;""==e.nome&&this.errors.push("Preencha o nome da instalação"),(e.desconto<0||e.desconto>100||""==e.desconto)&&this.errors.push("O valor de desconto deve ser entre 0% e 100%"),(e.bonus<0||""==e.bonus)&&this.errors.push("O valor do bônus deve ser preenchido com 0 ou qualquer número positivo")},async gravar(e){this.validar_campos(e),this.errors.length||(this.$store.commit("setIsLoading",!0),console.log(e),await $().put("/api/v1/clientes/"+e.id+"/",e).then((e=>{(0,te.toast)({message:"Cliente alterado",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.getClientes()})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1))},async apagar(e){this.$store.commit("setIsLoading",!0),console.log(e),await $()["delete"]("/api/v1/clientes/"+e.id+"/",e).then((e=>{(0,te.toast)({message:"Cliente removido da base de dados",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.getClientes()})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),await new Promise((e=>setTimeout(e,3e3))),this.$store.commit("setIsLoading",!1)},async novo(e){await this.validar_campos(e),this.errors.length||(this.$store.commit("setIsLoading",!0),console.log(e),await $().post("/api/v1/clientes/",e).then((e=>{(0,te.toast)({message:"Cliente adicionado",type:"is-success",dismissible:!0,pauseOnHover:!0,duration:2e3,position:"bottom-right"}),this.getClientes()})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),await new Promise((e=>setTimeout(e,3e3))),this.$store.commit("setIsLoading",!1))},async getClientes(){this.$store.commit("setIsLoading",!0),await $().get("/api/v1/clientes/").then((e=>{this.clientes=e.data,console.log(e)})).catch((e=>{401===e.response.status&&(console.log("Ticket expirado. Necessário novo login"),this.logout()),console.log(e)})),this.$store.commit("setIsLoading",!1)}}};const Ht=(0,x.Z)(jt,[["render",Rt],["__scopeId","data-v-584dc5f7"]]);var Et=Ht,Wt=o(65),Jt=(0,Wt.MT)({state:{access:"",refresh:"",isLoading:!1},mutations:{initializeStore(e){localStorage.getItem("access")?e.access=localStorage.getItem("access"):e.access=""},setAccess(e,t){e.access=t},setIsLoading(e,t){e.isLoading=t},removeToken(e){e.access=""}},actions:{},modules:{}});const Kt=[{path:"/",name:"home",component:T},{path:"/sign-up",name:"SignUp",component:ne},{path:"/log-in",name:"LogIn",component:Ce},{path:"/my-account",name:"MyAccount",component:Se,meta:{requireLogin:!0}},{path:"/clientes",name:"Clientes",component:Et,meta:{requireLogin:!0}},{path:"/faturas",name:"Faturas",component:tt,meta:{requireLogin:!0}},{path:"/fatura/:id",name:"Fatura",component:wt,meta:{requireLogin:!0}}],Yt=(0,L.p7)({history:(0,L.PO)("/static/"),routes:Kt});Yt.beforeEach(((e,t,o)=>{e.matched.some((e=>e.meta.requireLogin))&&!Jt.state.access?o({name:"LogIn",query:{to:e.path}}):o()}));var Zt=Yt;$().defaults.baseURL=window.location.origin,"http://localhost:8080"==$().defaults.baseURL&&($().defaults.baseURL="http://127.0.0.1:8000"),(0,a.ri)(I).use(Jt).use(Zt,$()).mount("#app")}},t={};function o(a){var n=t[a];if(void 0!==n)return n.exports;var s=t[a]={exports:{}};return e[a].call(s.exports,s,s.exports,o),s.exports}o.m=e,function(){var e=[];o.O=function(t,a,n,s){if(!a){var r=1/0;for(c=0;c<e.length;c++){a=e[c][0],n=e[c][1],s=e[c][2];for(var i=!0,l=0;l<a.length;l++)(!1&s||r>=s)&&Object.keys(o.O).every((function(e){return o.O[e](a[l])}))?a.splice(l--,1):(i=!1,s<r&&(r=s));if(i){e.splice(c--,1);var u=n();void 0!==u&&(t=u)}}return t}s=s||0;for(var c=e.length;c>0&&e[c-1][2]>s;c--)e[c]=e[c-1];e[c]=[a,n,s]}}(),function(){o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,{a:t}),t}}(),function(){o.d=function(e,t){for(var a in t)o.o(t,a)&&!o.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:t[a]})}}(),function(){o.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={143:0};o.O.j=function(t){return 0===e[t]};var t=function(t,a){var n,s,r=a[0],i=a[1],l=a[2],u=0;if(r.some((function(t){return 0!==e[t]}))){for(n in i)o.o(i,n)&&(o.m[n]=i[n]);if(l)var c=l(o)}for(t&&t(a);u<r.length;u++)s=r[u],o.o(e,s)&&e[s]&&e[s][0](),e[s]=0;return o.O(c)},a=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];a.forEach(t.bind(null,0)),a.push=t.bind(null,a.push.bind(a))}();var a=o.O(void 0,[998],(function(){return o(8123)}));a=o.O(a)})();
//# sourceMappingURL=app.fd59e7fd.js.map