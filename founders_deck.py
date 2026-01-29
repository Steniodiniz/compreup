import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="CompreUp Founders Deck")

# Código unificado e simplificado para evitar erro de renderização no Mac
deck_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { background-color: #f1f5f9; margin: 0; padding: 20px; font-family: sans-serif; }
        .slide-card { min-height: 500px; transition: all 0.3s ease; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useEffect } = React;

        const Icon = ({ name, className = "w-8 h-8" }) => {
            useEffect(() => { if(window.lucide) window.lucide.createIcons(); }, [name]);
            return <i data-lucide={name} className={className}></i>;
        };

        const App = () => {
            const [index, setIndex] = useState(0);

            const slides = [
                {
                    title: "Da Validação à Escala",
                    subtitle: "O Caminho CompreUp",
                    content: "Benchmark Cayena & Estratégia de Bootstrapping",
                    icon: "rocket",
                    type: "cover"
                },
                {
                    title: "O Farol: Case Cayena",
                    content: "Eles validaram que o PME está desesperado por digitalização. O mercado é de R$ 1 Bi GMV.",
                    icon: "trending-up",
                    type: "content"
                },
                {
                    title: "Fase 1: A Fortaleza",
                    content: "Foco em Fortaleza. Meta de 50-80 clientes e R$ 48k de MRR. Break-even operacional.",
                    icon: "anchor",
                    type: "content"
                },
                {
                    title: "Fase 2: Escala Tech",
                    content: "200-300 clientes. R$ 180k MRR. Automação de 90% dos pedidos.",
                    icon: "map",
                    type: "content"
                }
            ];

            const s = slides[index];

            return (
                <div className="flex flex-col items-center justify-center">
                    <div className="w-full max-w-4xl bg-white rounded-3xl shadow-xl overflow-hidden flex flex-col slide-card border border-gray-100">
                        {/* Progress Bar */}
                        <div className="h-2 bg-gray-100">
                            <div className="h-full bg-blue-600 transition-all duration-500" style={{width: `${((index + 1) / slides.length) * 100}%`}}></div>
                        </div>

                        {/* Slide Content */}
                        <div className="flex-1 p-12 flex flex-col justify-center items-center text-center">
                            <div className="bg-blue-50 p-6 rounded-full mb-6 text-blue-600">
                                <Icon name={s.icon} className="w-16 h-16" />
                            </div>
                            <h1 className="text-4xl font-black text-gray-800 mb-4">{s.title}</h1>
                            {s.subtitle && <h2 className="text-xl text-blue-600 mb-4">{s.subtitle}</h2>}
                            <p className="text-lg text-gray-600 max-w-lg">{s.content}</p>
                        </div>

                        {/* Nav Controls */}
                        <div className="p-8 bg-gray-50 flex justify-between items-center border-t">
                            <span className="text-xs font-bold text-gray-400">SLIDE {index + 1} DE {slides.length}</span>
                            <div className="flex gap-4">
                                <button 
                                    onClick={() => index > 0 && setIndex(index - 1)}
                                    className="p-3 rounded-full border bg-white hover:bg-gray-100 disabled:opacity-20"
                                    disabled={index === 0}
                                >
                                    <Icon name="chevron-left" />
                                </button>
                                <button 
                                    onClick={() => index < slides.length - 1 && setIndex(index + 1)}
                                    className="p-3 bg-slate-900 text-white rounded-full hover:bg-blue-600 disabled:opacity-20"
                                    disabled={index === slides.length - 1}
                                >
                                    <Icon name="chevron-right" />
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
"""

components.html(deck_html, height=700)