import Link from 'next/link'

import {
    SignedIn,
    SignOutButton
} from '@clerk/nextjs'

const Navbar = () => {
    const links = [
        { title: 'Calendar', url: '/calendar' },
        { title: 'Administration', url: '/admin', role: 'admin' }
    ];

    return (
        <header className='text-gray-600 body-font bg-white shadow'>
            <div className='container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center justify-between'>
                <nav className='md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center'>
                    <Link href='/'>
                        <div className='mr-5 cursor-pointer hover:text-gray-900'>
                            Calendar
                        </div>
                    </Link>
                    <Link href='/admin'>
                        <div className='mr-5 cursor-pointer hover:text-gray-900'>
                            Administration
                        </div>
                    </Link>
                    <SignedIn>
                        <SignOutButton />
                    </SignedIn>
                </nav>
            </div>
        </header>
    );
};

export default Navbar;
