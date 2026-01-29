import React, { useState } from 'react';
import { ChevronRight, ChevronLeft, Target, Users, TrendingUp, ShieldCheck, Map, Coins, Rocket, Anchor, LineChart, CheckCircle2, ArrowLeft, BookOpen } from 'lucide-react';

const FoundersDeck = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const slides = [
    {
      id: 0,
      type: 'cover',
      title: "Da Validação à Escala: O Caminho CompreUp",
      subtitle: "Benchmark Cayena & Estratégia de Bootstrapping",
      footer: "Reunião de Alinhamento Estratégico - Founders",
      icon: <Rocket className="w-20 h-20 text-blue-600" />
    },
    {
      id: 1,
      type: 'benchmark',
      title: "O Farol de Mercado: Case Cayena",
      content: (
        <div className="h-full flex flex-col justify-center">
          <div className="bg-blue-50 p-6 rounded-xl border-l-4 border-blue-600 mb-6 relative">
            <h3 className="text-xl font-bold text-blue-900 mb-2">O que a Cayena provou?</h3>
            <p className="text-gray-700 mb-4">Eles validaram que o PME de alimentação (padarias/restaurantes) está desesperado por digitalização e eficiência. O mercado existe e é gigantesco.</p>
            
            {/* Botão de Redirecionamento (Feature Nova) */}
            <button 
              onClick={() => setCurrentSlide(9)} // Redireciona para o slide extra (índice 9)
              className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors shadow-sm"
            >
              <BookOpen size={16} />
              Ver Análise Detalhada do Case
            </button>
          </div>
          
          <div className="grid grid-cols-3 gap-4 text-center">
            <div className="bg-white shadow-md p-4 rounded-lg">
              <div className="text-3xl font-bold text-gray-800">R$ 1 Bi</div>
              <div className="text-xs text-gray-500 uppercase">GMV Anualizado</div>
            </div>
            <div className="bg-white shadow-md p-4 rounded-lg">
              <div className="text-3xl font-bold text-gray-800">30k+</div>
              <div className="text-xs text-gray-500 uppercase">Compradores Ativos</div>
            </div>
            <div className="bg-white shadow-md p-4 rounded-lg">
              <div className="text-3xl font-bold text-gray-800">R$ 300 Mi</div>
              <div className="text-xs text-gray-500 uppercase">Captados (VC)</div>
            </div>
          </div>
          
          <div className="mt-8 text-center text-gray-500 text-sm italic">
            "A Cayena pavimentou a estrada. Agora nós vamos dirigir nela com um veículo mais eficiente."
          </div>
        </div>
      )
    },
    {
      id: 2,
      type: 'pivot',
      title: "Nosso Diferencial: A Evolução do Modelo",
      content: (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 h-full items-center">
          <div className="bg-gray-100 p-6 rounded-xl opacity-70">
            <h3 className="text-lg font-bold text-gray-600 mb-4 border-b pb-2">Modelo Tradicional (Cayena)</h3>
            <ul className="space-y-4">
              <li className="flex items-center gap-2 text-gray-600">
                <Coins size={20} /> Monetização via <strong>Comissão (Take Rate)</strong>
              </li>
              <li className="flex items-center gap-2 text-gray-600">
                <Users size={20} /> Cliente é o <strong>Fornecedor</strong>
              </li>
              <li className="flex items-center gap-2 text-gray-600">
                <Anchor size={20} /> Conflito de Interesse (Vender o mais caro)
              </li>
            </ul>
          </div>

          <div className="bg-green-50 p-6 rounded-xl border-2 border-green-500 shadow-xl transform scale-105">
            <div className="absolute -top-3 right-4 bg-green-600 text-white px-3 py-1 text-xs font-bold rounded-full uppercase">CompreUp</div>
            <h3 className="text-lg font-bold text-green-800 mb-4 border-b border-green-200 pb-2">Nosso Modelo (SaaS)</h3>
            <ul className="space-y-4">
              <li className="flex items-center gap-2 text-gray-800">
                <ShieldCheck size={20} className="text-green-600" /> Monetização via <strong>Assinatura Recorrente</strong>
              </li>
              <li className="flex items-center gap-2 text-gray-800">
                <Users size={20} className="text-green-600" /> Cliente é o <strong>Comprador</strong>
              </li>
              <li className="flex items-center gap-2 text-gray-800">
                <Target size={20} className="text-green-600" /> Alinhamento Total (Vender o mais barato)
              </li>
            </ul>
          </div>
        </div>
      )
    },
    {
      id: 3,
      type: 'strategy',
      title: "A Estratégia: Bootstrapping vs Blitzscaling",
      content: (
        <div className="space-y-6">
          <p className="text-gray-600 text-lg">
            Não vamos queimar caixa para crescer a qualquer custo. Vamos crescer com a receita do cliente e com o recurso da subvenção (R$ 500k) focado em produto.
          </p>

          <div className="grid grid-cols-2 gap-8 mt-6">
            <div className="border-r border-gray-200 pr-4">
              <h4 className="font-bold text-red-600 mb-2">❌ O que EVITAREMOS</h4>
              <ul className="text-sm text-gray-600 space-y-2">
                <li>• Custo de Aquisição (CAC) alto via anúncios pagos.</li>
                <li>• Subsídio de preço com dinheiro de caixa.</li>
                <li>• Expansão para novas cidades antes da hora.</li>
                <li>• Equipes inchadas.</li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold text-green-600 mb-2">✅ O Jeito CompreUp</h4>
              <ul className="text-sm text-gray-600 space-y-2">
                <li>• Crescimento via Indicação (Viralidade B2B).</li>
                <li>• Foco obsessivo em Retenção (Churn Negativo).</li>
                <li>• Estrutura Asset-Light (Sem estoque).</li>
                <li>• Reinvestimento do lucro da assinatura.</li>
              </ul>
            </div>
          </div>
        </div>
      )
    },
    {
      id: 4,
      type: 'phase1',
      title: "Fase 1: A Fortaleza (0-12 Meses)",
      content: (
        <div className="bg-white h-full flex flex-col">
          <div className="flex items-center gap-4 mb-6">
            <div className="bg-orange-100 p-3 rounded-full"><Anchor className="text-orange-600 w-8 h-8" /></div>
            <div>
              <h3 className="text-xl font-bold text-gray-800">Validação & Unit Economics</h3>
              <p className="text-sm text-gray-500">Foco: Grande Fortaleza | Mix: Ovos, Frango, Curva A</p>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">50-80</span>
              <span className="text-xs text-gray-500 uppercase">Clientes</span>
            </div>
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">R$ 48k</span>
              <span className="text-xs text-gray-500 uppercase">MRR Estimado</span>
            </div>
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">Manual</span>
              <span className="text-xs text-gray-500 uppercase">Tecnologia (MVP)</span>
            </div>
          </div>

          <div className="bg-orange-50 p-4 rounded-lg border border-orange-200 mt-auto">
            <h4 className="font-bold text-orange-800 mb-2 text-sm uppercase">Meta Crítica</h4>
            <p className="text-gray-700 text-sm">Atingir o Break-even operacional. A subvenção de R$ 500k financia o desenvolvimento da plataforma robusta enquanto operamos no "Concierge".</p>
          </div>
        </div>
      )
    },
    {
      id: 5,
      type: 'phase2',
      title: "Fase 2: Expansão Regional (12-24 Meses)",
      content: (
        <div className="bg-white h-full flex flex-col">
          <div className="flex items-center gap-4 mb-6">
            <div className="bg-blue-100 p-3 rounded-full"><Map className="text-blue-600 w-8 h-8" /></div>
            <div>
              <h3 className="text-xl font-bold text-gray-800">Escala Tecnológica</h3>
              <p className="text-sm text-gray-500">Foco: Região Metropolitana | Mix: Ampliação para Mercearia</p>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">200-300</span>
              <span className="text-xs text-gray-500 uppercase">Clientes</span>
            </div>
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">R$ 180k</span>
              <span className="text-xs text-gray-500 uppercase">MRR Estimado</span>
            </div>
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">Auto</span>
              <span className="text-xs text-gray-500 uppercase">Tecnologia</span>
            </div>
          </div>

          <div className="bg-blue-50 p-4 rounded-lg border border-blue-200 mt-auto">
            <h4 className="font-bold text-blue-800 mb-2 text-sm uppercase">Meta Crítica</h4>
            <p className="text-gray-700 text-sm">Automação de 90% dos pedidos. O efeito de rede começa a operar (clientes indicam clientes). Dados começam a gerar relatórios preditivos.</p>
          </div>
        </div>
      )
    },
    {
      id: 6,
      type: 'phase3',
      title: "Fase 3: O Sistema Operacional (24-48 Meses)",
      content: (
        <div className="bg-white h-full flex flex-col">
          <div className="flex items-center gap-4 mb-6">
            <div className="bg-purple-100 p-3 rounded-full"><TrendingUp className="text-purple-600 w-8 h-8" /></div>
            <div>
              <h3 className="text-xl font-bold text-gray-800">Ecossistema & Fintech</h3>
              <p className="text-sm text-gray-500">Foco: Nordeste | Mix: BPO de Compras e Serviços Financeiros</p>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">1.000+</span>
              <span className="text-xs text-gray-500 uppercase">Clientes</span>
            </div>
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">R$ 600k+</span>
              <span className="text-xs text-gray-500 uppercase">MRR Estimado</span>
            </div>
            <div className="bg-gray-50 p-4 rounded text-center border border-gray-200">
              <span className="block text-2xl font-bold text-gray-800">Fintech</span>
              <span className="text-xs text-gray-500 uppercase">Expansão</span>
            </div>
          </div>

          <div className="bg-purple-50 p-4 rounded-lg border border-purple-200 mt-auto">
            <h4 className="font-bold text-purple-800 mb-2 text-sm uppercase">Meta Crítica</h4>
            <p className="text-gray-700 text-sm">Tornar-se o "Departamento de Compras" terceirizado do cliente. Receita vem de SaaS + Crédito + Antecipação.</p>
          </div>
        </div>
      )
    },
    {
      id: 7,
      type: 'financials',
      title: "Crescimento Sustentável (MRR)",
      content: (
        <div className="flex flex-col h-full justify-center items-center">
          <div className="w-full max-w-2xl relative h-64 flex items-end justify-between px-8 border-b-2 border-gray-300 pb-2">
            
            {/* Year 1 Bar */}
            <div className="flex flex-col items-center group w-1/4">
              <div className="mb-2 text-gray-600 font-bold opacity-0 group-hover:opacity-100 transition-opacity duration-300">R$ 360k/ano</div>
              <div className="w-full bg-orange-400 rounded-t-lg transition-all duration-1000 ease-out h-16 relative hover:bg-orange-500">
                 <div className="absolute top-2 left-0 right-0 text-center text-white font-bold text-xs">Fase 1</div>
              </div>
              <div className="mt-4 text-gray-600 font-semibold">Ano 1</div>
            </div>

            {/* Year 2 Bar */}
            <div className="flex flex-col items-center group w-1/4">
              <div className="mb-2 text-gray-600 font-bold opacity-0 group-hover:opacity-100 transition-opacity duration-300">R$ 1.44 Mi/ano</div>
              <div className="w-full bg-blue-500 rounded-t-lg transition-all duration-1000 ease-out h-32 relative hover:bg-blue-600">
                <div className="absolute top-2 left-0 right-0 text-center text-white font-bold text-xs">Fase 2</div>
              </div>
              <div className="mt-4 text-gray-600 font-semibold">Ano 2</div>
            </div>

            {/* Year 3 Bar */}
            <div className="flex flex-col items-center group w-1/4">
              <div className="mb-2 text-gray-600 font-bold opacity-0 group-hover:opacity-100 transition-opacity duration-300">R$ 4.3 Mi/ano</div>
              <div className="w-full bg-purple-600 rounded-t-lg transition-all duration-1000 ease-out h-56 relative hover:bg-purple-700 shadow-lg shadow-purple-200">
                <div className="absolute top-2 left-0 right-0 text-center text-white font-bold text-xs">Fase 3</div>
              </div>
              <div className="mt-4 text-gray-600 font-semibold">Ano 3</div>
            </div>
            
          </div>
          <div className="mt-8 text-center text-sm text-gray-500 max-w-lg">
            *Projeção baseada apenas na receita de assinaturas, reinvestindo 100% do lucro operacional na expansão.
          </div>
        </div>
      )
    },
    {
      id: 8,
      type: 'conclusion',
      title: "Próximos Passos",
      subtitle: "Execução Imediata",
      content: (
        <div className="space-y-6">
           <div className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-green-500">
             <h3 className="text-lg font-bold text-gray-800 mb-2">1. Iniciar MVP Concierge</h3>
             <p className="text-gray-600">Focar nos 20-50 primeiros clientes em Fortaleza. Validar a entrega fracionada com fornecedores.</p>
           </div>
           <div className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-blue-500">
             <h3 className="text-lg font-bold text-gray-800 mb-2">2. Aplicar Recursos da Subvenção</h3>
             <p className="text-gray-600">Direcionar os R$ 500k para construção da tecnologia proprietária (ativo) e capital de giro inicial.</p>
           </div>
           <div className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-purple-500">
             <h3 className="text-lg font-bold text-gray-800 mb-2">3. Monitorar o Churn</h3>
             <p className="text-gray-600">A métrica principal desta fase não é faturamento, é retenção. Se o cliente fica, o modelo funciona.</p>
           </div>
        </div>
      )
    },
    // NOVO SLIDE OCULTO (ID 9)
    {
      id: 9,
      type: 'detail',
      title: "Deep Dive: O Case Cayena",
      subtitle: "Benchmark em Detalhes",
      content: (
        <div className="h-full flex flex-col">
          <button 
            onClick={() => setCurrentSlide(1)} 
            className="self-start mb-6 flex items-center gap-2 text-blue-600 hover:text-blue-800 font-bold transition-colors"
          >
            <ArrowLeft size={20} /> Voltar para o Benchmark
          </button>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 flex-1 overflow-y-auto">
            <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
              <h3 className="text-lg font-bold text-blue-900 mb-4 flex items-center gap-2">
                <CheckCircle2 size={20}/> O Que Fizeram Certo?
              </h3>
              <ul className="space-y-3 text-sm text-gray-700">
                <li><strong>Timing Perfeito:</strong> Lançaram durante a pandemia, quando restaurantes precisavam digitalizar compras.</li>
                <li><strong>Estoque Zero (Asset Light):</strong> Conectam o estoque do fornecedor direto ao cliente, sem warehouses gigantes (reduzindo Capex).</li>
                <li><strong>Mix Infinito:</strong> Oferecem de tudo, virando "One Stop Shop".</li>
              </ul>
            </div>

            <div className="bg-orange-50 p-6 rounded-xl border border-orange-200">
              <h3 className="text-lg font-bold text-orange-900 mb-4 flex items-center gap-2">
                <Target size={20}/> Onde Deixam a Desejar? (Nossa Chance)
              </h3>
              <ul className="space-y-3 text-sm text-gray-700">
                <li><strong>Modelo de Corretagem:</strong> Cobram comissão do fornecedor (Take Rate), o que impede transparência real de preço.</li>
                <li><strong>Logística Complexa:</strong> Ao escalar muito rápido, sofrem com atrasos e ruptura, gerando churn.</li>
                <li><strong>Atendimento Impessoal:</strong> Para o pequeno dono de padaria, virou um "call center".</li>
              </ul>
            </div>

            <div className="col-span-1 md:col-span-2 bg-blue-600 text-white p-6 rounded-xl shadow-lg mt-auto">
              <h3 className="font-bold text-lg mb-2">A Lição para a CompreUp</h3>
              <p className="text-blue-100 text-sm">
                A Cayena provou que o modelo "Asset Light" funciona. A CompreUp vai aprimorar esse modelo focando na **Transparência (Assinatura)** e na **Inteligência de Gestão**, criando uma barreira de saída (moat) que a Cayena não possui.
              </p>
            </div>
          </div>
        </div>
      )
    }
  ];

  // Logic to prevent standard navigation to the hidden slide (index 9)
  const mainSlidesCount = slides.length - 1; // 9 main slides

  const nextSlide = () => {
    // Blocks navigation if current slide is the last MAIN slide (Conclusion)
    if (currentSlide < mainSlidesCount - 1) setCurrentSlide(currentSlide + 1);
  };

  const prevSlide = () => {
    // If in detail slide (9), go back to main slide (1) or use standard logic
    if (currentSlide === 9) {
        setCurrentSlide(1);
    } else if (currentSlide > 0) {
        setCurrentSlide(currentSlide - 1);
    }
  };

  const currentData = slides[currentSlide];

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-slate-100 p-4 font-sans text-gray-900">
      {/* Deck Container */}
      <div className="w-full max-w-5xl bg-white rounded-2xl shadow-2xl overflow-hidden flex flex-col" style={{ aspectRatio: '16/9', minHeight: '600px' }}>
        
        {/* Header / Progress */}
        <div className="bg-slate-900 h-2 w-full">
          <div 
            className={`h-full transition-all duration-500 ease-out ${
              currentData.type === 'detail' ? 'bg-indigo-600' :
              currentData.type.includes('phase') ? 'bg-orange-500' : 
              currentData.type === 'financials' ? 'bg-green-500' : 'bg-blue-600'
            }`}
            // Progress bar stays full on detail slide or calculates normally for others
            style={{ width: currentSlide === 9 ? '100%' : `${((currentSlide + 1) / mainSlidesCount) * 100}%` }}
          ></div>
        </div>

        {/* Slide Content Area */}
        <div className="flex-1 p-8 md:p-12 flex flex-col relative overflow-y-auto">
          
          {currentData.type === 'cover' ? (
            <div className="flex flex-col items-center justify-center h-full text-center space-y-6 animate-in fade-in duration-700">
              <div className="bg-blue-50 p-8 rounded-full mb-4 shadow-inner">
                {currentData.icon}
              </div>
              <h1 className="text-4xl md:text-5xl font-extrabold text-slate-800 tracking-tight">{currentData.title}</h1>
              <h2 className="text-xl md:text-2xl text-blue-600 font-medium">{currentData.subtitle}</h2>
              <div className="mt-12 pt-8 border-t border-gray-100 w-1/2 mx-auto">
                <p className="text-sm text-gray-400 font-mono font-semibold">{currentData.footer}</p>
              </div>
            </div>
          ) : (
            <div className="h-full flex flex-col animate-in slide-in-from-right duration-500">
              {/* Hide Header on Detail Slide to maximize space or keep consistent? Keeping consistent but removing number bar */}
              <div className="flex items-center gap-4 mb-8 pb-4 border-b border-gray-100">
                {currentData.type !== 'detail' && (
                  <div className={`w-2 h-10 rounded-sm ${
                    currentData.type.includes('phase') ? 'bg-orange-500' : 'bg-blue-600'
                  }`}></div>
                )}
                <h2 className="text-3xl font-bold text-slate-800">{currentData.title}</h2>
              </div>
              <div className="flex-1">
                {currentData.content}
              </div>
            </div>
          )}

        </div>

        {/* Controls */}
        {/* Hide standard controls on Detail Slide to force use of "Back" button inside content */}
        {currentData.type !== 'detail' && (
          <div className="bg-slate-50 p-4 border-t border-gray-200 flex justify-between items-center">
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">Estratégia CompreUp</span>
              <span className="text-xs text-slate-300">|</span>
              <span className="text-xs text-slate-400 font-mono">Slide {currentSlide + 1}/{mainSlidesCount}</span>
            </div>
            <div className="flex gap-4 mr-4">
              <button 
                onClick={prevSlide} 
                disabled={currentSlide === 0}
                className={`p-3 rounded-full transition-all ${currentSlide === 0 ? 'text-gray-300 cursor-not-allowed' : 'bg-white text-slate-700 hover:bg-blue-50 hover:text-blue-600 shadow-sm border border-gray-200'}`}
              >
                <ChevronLeft size={24} />
              </button>
              <button 
                onClick={nextSlide} 
                // Disable next on the last MAIN slide (index 8) to prevent accidental navigation to detail slide
                disabled={currentSlide === mainSlidesCount - 1}
                className={`p-3 rounded-full transition-all ${currentSlide === mainSlidesCount - 1 ? 'text-gray-300 cursor-not-allowed' : 'bg-slate-900 text-white hover:bg-blue-600 shadow-lg hover:shadow-xl hover:scale-105'}`}
              >
                <ChevronRight size={24} />
              </button>
            </div>
          </div>
        )}
      </div>

      <div className="mt-6 text-gray-400 text-xs font-medium">
        Use as setas para navegar • Foco em Execução
      </div>
    </div>
  );
};

export default FoundersDeck;