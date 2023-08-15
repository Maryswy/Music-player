import './globals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Header from './components/Header'
import Head from 'next/head'
import Footer from './components/Footer'
const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: '',
  description: '',
  keywords: '',
  author: '',
}
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <Head>
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
        <meta name="keywords" content={metadata.keywords} />
        <meta name="author" content={metadata.author} />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <body>
        <Header />
        {children}
        <Footer />
      </body>
    </html>
  )
}