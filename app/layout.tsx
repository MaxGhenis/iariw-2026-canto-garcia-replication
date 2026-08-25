import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Wealth taxation in Spain — IARIW 2026 discussant slides',
  description:
    'Discussant presentation of Cantó & García-Rodríguez (2026), Progressivity and Redistribution of Wealth Taxation in Spain',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
