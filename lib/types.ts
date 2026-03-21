export interface FoodSource {
  id: string;
  text: string;
  region: string;
  type: string;
  score: number;
}

export interface RAGResponse {
  sources: FoodSource[];
  answer: string;
}

export interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  sources?: FoodSource[];
  isLoading?: boolean;
}
