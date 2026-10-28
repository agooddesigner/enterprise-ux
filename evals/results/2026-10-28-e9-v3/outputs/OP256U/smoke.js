const fs=require('fs');
const html=fs.readFileSync('/tmp/ux-e9v3b/OP256U/support-staffing-dashboard.html','utf8');
const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
const els={};
const mk=()=>({innerHTML:'',textContent:'',style:{},dataset:{},classList:{add(){},remove(){}},addEventListener(){},querySelector(){return mk()},querySelectorAll(){return []},showModal(){},scrollIntoView(){},open:false,value:''});
global.document={querySelector:s=>els[s]??(els[s]=mk()),addEventListener(){}};
global.location={search:'',pathname:'/'};
global.history={replaceState(){}};
global.setTimeout=()=>0;global.clearTimeout=()=>{};
const run=new Function(js+`
for(const s of ['ready','loading','error','empty']){S.state=s;renderAll();}
S.state='ready';S.view='short';renderAll();apply(['m1','m2']);
return {sla:[totalSla(false),totalSla(true)]};`);
const r=run();
console.log('OK',r);
console.log(els['#headline'].innerHTML);
console.log(els['#hero'].innerHTML.replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').slice(0,400));
const m=els['#hourly'].innerHTML.match(/class="insight">(.*?)<\/p>/);
console.log(m&&m[1]);
