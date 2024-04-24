public class Notebook extends Computador{
    private int polegadasTela;
    public Notebook(int gbMemoria, int numProcessadores, int polegadasTela) {
        super(gbMemoria, numProcessadores);
        this.polegadasTela = polegadasTela;
    }


    @Override
    public double calculaValor(){
        return GbMemoria * 250 + NumProcessadores * 500 + polegadasTela * 100;
    }



}
