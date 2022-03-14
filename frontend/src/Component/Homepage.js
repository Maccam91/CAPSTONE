import React from 'react'

function HomePage(){

    return (
        <div>
            <h2>Hello and Welcome to Fireside</h2>
            <form>
                <h4>Email</h4>
                <input type='email'/>
                <br/>
                <h4>UserName</h4>
                <input type='text'/>
                <br/>
                <h4>Password</h4>
                <input type='password'/>
                <br/>
                <input type='submit' value='Create Account'/>
            </form>
        </div>
    )
}


export default HomePage