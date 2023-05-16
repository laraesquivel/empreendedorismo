import { Link } from "react-router-dom";
import { Logo } from "../assets/Logo";

// cellphone_zap, bairro_id

export function SignUp() {
  return (
    <div className="flex items-center justify-center bg-gray-200 h-full w-full">
      <div className="w-[307px] h-[666px] mt-14 bg-[url('../assets/Cadastro.svg')] flex flex-col justify-center items-center  mb-20 rounded-lg">
        <div className="h-[150px] pt-12">
          <Logo  />
        </div>

        <form action="">
        <div className=" flex flex-col space-y-6 h-[300px] w-[230px] overflow-auto">
          <input
              type="text"
              placeholder="NOME"
              className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
              required
            />

          <input
              type="email"
              placeholder="EMAIL"
              className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
              required
            />
           <input
              type="password"
              placeholder="SENHA"
              className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
              required
            />
            <input
              type="number"
              placeholder="TELEFONE"
              className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
              required
            />
             <input
              type="number"
              placeholder="CPF"
              className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
              required
            />
             <input
              type="number"
              placeholder="CEP"
              className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
              required
            /> 
            <input
            type="text"
            placeholder="BAIRRO"
            className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
          />
            <input
            type="text"
            placeholder="RUA"
            className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
          />
          <input
            type="number"
            placeholder="Nº DA RESIDÊNCIA"
            className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
          />
          <input
            type="text"
            placeholder="COMPLEMENTO"
            className="text-sm rounded-lg outline-none placeholder:text-black placeholder:opacity-50 placeholder:pl-2 placeholder:font-semibold border-b-[3px] border-black bg-gray-100"
          />


        </div>

        <div className="flex flex-col  justify-center items-center pt-6">
          <button
            className=" rounded-lg border-y-[3px] border-black w-[200px] h-[52px] font-bold"
                >
                REGISTRAR
          </button>
          <div className='pt-2'>
            <Link to={'/'} className='font-bold text-xs border-b-2 border-black'>LOGIN</Link>
          </div>  
        </div>
        </form>
      </div>
    </div>
  );
}
