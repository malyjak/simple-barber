import {
    SignIn,
    SignedOut,
    SignedIn
} from '@clerk/nextjs'

const Admin = () => {
    return (
        <>
            <SignedOut>
                <div className='centered-div'>
                    <SignIn />
                </div>
            </SignedOut>
            <SignedIn>
                <div className='centered-div'>
                    <h3>Welcome to admin page!</h3>
                    <h4>Services:</h4>
                </div>
            </SignedIn>
        </>
    );
};

export default Admin;
