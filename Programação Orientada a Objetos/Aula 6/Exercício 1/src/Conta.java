public class Conta {
    private String nome;
    private double saldo;

    /**
     * @return the saldo
     */
    public double getSaldo() {
        return saldo;
    }
    /**
     * @param saldo the saldo to set
     */
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    //Métodos
    public void depositar(double valor) throws Exception{
        try {
            if (valor < 0) {
                throw new Exception("Digite um número válido!");
                
            }
        } finally{}
    }
    public void sacar(double valor){}
    public void transferir(double valor, Conta contaDestinatária){}
    @Override
    public String toString() {
        return "Conta [nome=" + nome + ", saldo=" + saldo + "]";
    }

    

}
