public abstract class Computador {
    protected int GbMemoria;
    protected int NumProcessadores;

    

    /**
     * @param gbMemoria
     * @param numProcessadores
     */
    public Computador(int gbMemoria, int numProcessadores) {
        GbMemoria = gbMemoria;
        NumProcessadores = numProcessadores;
    }

    



    @Override
    public String toString() {
        return "Computador [GbMemoria=" + GbMemoria + ", NumProcessadores=" + NumProcessadores + "]";
    }





    public abstract double calculaValor();

}
