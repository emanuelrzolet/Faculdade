public class Conta {
    int numero;
    String titular;
    float saldo;
    float limite = saldo + saldo * 0.1f;

    

    //Construtor
    /**
     * @param numero
     * @param titular
     * @param saldo
     */
    public Conta(int numero, String titular, float saldo) {
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
    }


    //Métodos
    Boolean transferir(Conta conta1, Conta conta2, float valor){
        if ((conta1.saldo + conta1.limite) > valor) {
            conta1.saldo -= valor;
            conta2.saldo += valor;
            System.out.println("Valor enviado para a conta destinatária!");
            return true;

        }
        else{
            return false;}
        
    }
    Boolean sacar(float valor){
        if ((saldo + limite) > valor) {
            saldo  -= valor;
            return true;

            
            
        }
        else{
            System.out.println("Não há saldo suficiente!");
            return false;
        }
    };
    Boolean deposita(float valor){
        saldo += valor;
        System.out.println("O valor foi depositado");
        return true;
    };
    void info(){
        System.out.println("Titular: " + titular);
        System.out.println("Número: " + numero);
        System.out.println("Saldo: " + saldo);
        System.out.println("Limite: " + limite);
    };

}
