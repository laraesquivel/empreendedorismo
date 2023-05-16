import { Link } from 'react-router-dom';
import { Logo } from '../assets/Logo';
import { Google } from '../assets/Google';
import { Apple } from '../assets/Apple';
import { Facebook } from '../assets/Facebook';

export function Login() {
  return (
    <div className="flex items-center justify-center bg-gray-200 h-full w-full">
      <div className="w-[307px] h-[666px] mt-14 bg-[url('../assets/Login.svg')] flex flex-col justify-center items-center  mb-20 rounded-lg">
        <div className="h-[200px] pt-12">
          <Logo  />
        </div>

        <form className="flex flex-col space-y-8 h-[250px] pt-16">
          <input
            type="email"
            placeholder="EMAIL"
            className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
            required
          />
          <input
            type="email"
            placeholder="SENHA"
            className=" w-[230px] text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black  bg-gray-100"
            required
          />
          <div className='flex flex-col items-center pt-14'>
            <button
              className=" rounded-lg border-y-[3px] border-black w-[200px] h-[52px] font-bold"
                >
                ENTRAR
            </button>
          </div>
        </form>

        <div className='flex flex-col items-center justify-center pt-6 '>
                <div className='pt-2'>
                    <Link to={'/signUp'} className='font-bold text-xs border-b-2 border-black'>REGISTRAR</Link>
                </div>  

            <div className='flex flex-row space-x-8 pt-2'>
                <div> 
                    <Link to={'/'}><Google/></Link>
                </div>

                <div>
                    <Link to={'/'}><Apple/></Link>
                </div>
                <div>
                    <Link to={'/'}><Facebook/></Link>
                </div>
            </div>
        </div>

      </div>
    </div>
  );
}
