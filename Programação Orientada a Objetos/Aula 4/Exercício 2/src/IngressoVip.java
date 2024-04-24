public class IngressoVip extends Ingresso{
    private double adicional;

    public IngressoVip(String nomeEvento, double valor, double adicional) {
        super(nomeEvento, valor);
    }

    @Override
    public void imprimir() {
        // TODO Auto-generated method stub
        super.imprimir();
        System.out.println("Adicional do ingresso VIP: " + adicional);
    }



}
