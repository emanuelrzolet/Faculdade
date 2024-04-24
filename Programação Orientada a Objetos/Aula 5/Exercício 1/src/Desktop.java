public class Desktop extends Computador {
    private double acessorios;


    public Desktop(int gbMemoria, int numProcessadores, double acessorios) {
        super(gbMemoria, numProcessadores);
        this.acessorios = acessorios;
    }



    


    @Override
    public double calculaValor() {
        return GbMemoria * 200 + NumProcessadores * 400 + acessorios;
    }






    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString() + " Acessórios: " + acessorios;
    }

    

}
