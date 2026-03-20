import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Drugagent UI",
  description: "Human-in-the-loop UI for the multi-agent drug discovery workflow.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-neutral-950 text-neutral-100 antialiased">{children}</body>
    </html>
  );
}
