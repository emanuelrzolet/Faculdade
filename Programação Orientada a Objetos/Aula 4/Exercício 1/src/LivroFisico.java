public class LivroFisico extends Livro{
    private int tiragem, peso;

    public LivroFisico(String titulo, String genero, int edicao, Autor autor, int tiragem, int peso) {
        super(titulo, genero, edicao, autor);
        
        this.tiragem = tiragem;
        this.peso = peso;
    }


    /**
     * @return the tiragem
     */
    public int getTiragem() {
        return tiragem;
    }

    /**
     * @param tiragem the tiragem to set
     */
    public void setTiragem(int tiragem) {
        this.tiragem = tiragem;
    }

    /**
     * @return the peso
     */
    public int getPeso() {
        return peso;
    }

    /**
     * @param peso the peso to set
     */
    public void setPeso(int peso) {
        this.peso = peso;
    }


}
