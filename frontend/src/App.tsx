import { useState } from "react";
import { Scale, FileText, Search, ChevronRight, Globe } from "lucide-react";

const CATEGORIES = [
  { id: "consumer", labelPt: "Direitos do Consumidor", labelEn: "Consumer Rights", icon: "🛒" },
  { id: "labour",   labelPt: "Direitos Trabalhistas",  labelEn: "Labour Rights",   icon: "👷" },
  { id: "housing",  labelPt: "Direito à Moradia",      labelEn: "Housing Rights",  icon: "🏠" },
  { id: "civil",    labelPt: "Direitos Civis",         labelEn: "Civil Rights",    icon: "⚖️" },
];

export default function App() {
  const [lang, setLang] = useState<"pt" | "en">("pt");
  const [category, setCategory] = useState("general");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const t = {
    title:       lang === "pt" ? "Cidadania AI"                                    : "Cidadania AI",
    subtitle:    lang === "pt" ? "Conheça seus direitos. Aja com confiança."       : "Know your rights. Act with confidence.",
    placeholder: lang === "pt" ? "Qual é a sua dúvida sobre seus direitos?"       : "What is your question about your rights?",
    ask:         lang === "pt" ? "Perguntar"                                       : "Ask",
    disclaimer:  lang === "pt" ? "Esta resposta é informativa e não constitui aconselhamento jurídico." : "This response is informational and does not constitute legal advice.",
  };

  async function handleAsk() {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    try {
      const res = await fetch("http://localhost:8000/api/v1/rights/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, category, language: lang }),
      });
      const data = await res.json();
      setAnswer(data.answer);
    } catch {
      setAnswer(lang === "pt" ? "Erro ao conectar com o servidor." : "Error connecting to the server.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 text-white">
      {/* Header */}
      <header className="border-b border-slate-700 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Scale className="w-6 h-6 text-amber-400" />
          <span className="font-bold text-xl">{t.title}</span>
        </div>
        <button
          onClick={() => setLang(lang === "pt" ? "en" : "pt")}
          className="flex items-center gap-1 text-sm text-slate-300 hover:text-white transition-colors"
        >
          <Globe className="w-4 h-4" />
          {lang === "pt" ? "EN" : "PT"}
        </button>
      </header>

      <main className="max-w-3xl mx-auto px-6 py-12">
        {/* Hero */}
        <div className="text-center mb-10">
          <h1 className="text-4xl font-bold mb-3">{t.subtitle}</h1>
          <p className="text-slate-400 text-lg">
            {lang === "pt"
              ? "Pergunte sobre seus direitos em linguagem simples e receba orientação baseada na legislação."
              : "Ask about your rights in plain language and receive guidance grounded in legislation."}
          </p>
        </div>

        {/* Category selector */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
          {CATEGORIES.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setCategory(cat.id)}
              className={`p-3 rounded-xl border text-sm font-medium transition-all ${
                category === cat.id
                  ? "border-amber-400 bg-amber-400/10 text-amber-400"
                  : "border-slate-600 hover:border-slate-400 text-slate-300"
              }`}
            >
              <span className="block text-2xl mb-1">{cat.icon}</span>
              {lang === "pt" ? cat.labelPt : cat.labelEn}
            </button>
          ))}
        </div>

        {/* Question input */}
        <div className="flex gap-3 mb-6">
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder={t.placeholder}
            rows={3}
            className="flex-1 bg-slate-700 border border-slate-600 rounded-xl px-4 py-3 text-white placeholder-slate-400 resize-none focus:outline-none focus:border-amber-400 transition-colors"
          />
          <button
            onClick={handleAsk}
            disabled={loading || !question.trim()}
            className="px-5 py-3 bg-amber-400 text-slate-900 font-semibold rounded-xl hover:bg-amber-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
          >
            {loading ? (
              <span className="animate-spin">⟳</span>
            ) : (
              <>
                {t.ask}
                <ChevronRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>

        {/* Answer */}
        {answer && (
          <div className="bg-slate-700/50 border border-slate-600 rounded-xl p-6">
            <p className="text-slate-100 leading-relaxed whitespace-pre-wrap">{answer}</p>
            <p className="mt-4 text-xs text-slate-400 italic">{t.disclaimer}</p>
          </div>
        )}
      </main>
    </div>
  );
}
