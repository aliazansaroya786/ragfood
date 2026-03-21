import { Header } from "@/components/header";
import { ChatInterface } from "@/components/chat-interface";

export default function Home() {
  return (
    <div className="flex h-dvh flex-col">
      <Header />
      <main className="flex-1 overflow-hidden">
        <ChatInterface />
      </main>
      <footer className="border-t py-3 text-center text-xs text-muted-foreground">
        Food RAG uses retrieval-augmented generation to answer your culinary
        questions
      </footer>
    </div>
  );
}
