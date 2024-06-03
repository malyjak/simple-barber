import './globals.css'
import { Inter } from 'next/font/google'

import {
    ClerkProvider,
    SignInButton,
    SignedIn,
    SignedOut,
    UserButton
} from '@clerk/nextjs'

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
        // <html lang="en">
        // <body className={inter.className}>{children}</body>
        // </html>
        <ClerkProvider>
            <html lang='en'>
                <body>
                    <SignedOut>
                        <SignInButton />
                    </SignedOut>
                    <SignedIn>
                        <UserButton />
                    </SignedIn>
                    {children}
                </body>
            </html> 
        </ClerkProvider>
    )
}
