import './globals.css'
import { Inter } from 'next/font/google'
import Navbar from '../components/Navbar'

import { ClerkProvider } from '@clerk/nextjs'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
    title: 'Simple Barber',
    description: 'Simple reservation system for barbers written in Next.js that uses FastAPI with SQLAlchemy as the API backend',
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <ClerkProvider appearance={{
            elements: {
                footer: "hidden",
            },
          }}>
            <html lang="en">
                <body>
                    <Navbar />
                    {children}
                </body>
            </html> 
        </ClerkProvider>
    )
}
