import { UtensilsCrossed } from "lucide-react";

export function Header() {
  return (
    <header className="border-b bg-background">
      <div className="mx-auto flex h-16 max-w-4xl items-center justify-between px-4">
        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary">
            <UtensilsCrossed className="h-5 w-5 text-primary-foreground" />
          </div>
          <div className="flex flex-col">
            <span className="text-lg font-semibold leading-tight">
              Food RAG
            </span>
            <span className="text-xs text-muted-foreground">
              AI-Powered Food Knowledge
            </span>
          </div>
        </div>
        <nav className="hidden items-center gap-6 sm:flex">
          <span className="text-sm text-muted-foreground">
            Powered by Upstash Vector & Groq
          </span>
        </nav>
      </div>
    </header>
  );
}
