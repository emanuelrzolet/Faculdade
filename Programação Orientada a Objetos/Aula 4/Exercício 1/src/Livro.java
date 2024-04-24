public class Livro {
    private String titulo, genero;
    private int edicao;
    private Autor autor;



    //Construtor
    

    //Getters e Setters
    /**
     * @return the titulo
     */
    public String getTitulo() {
        return titulo;
    }
    /**
     * @param titulo
     * @param genero
     * @param edicao
     * @param autor
     */
    public Livro(String titulo, String genero, int edicao, Autor autor) {
        this.titulo = titulo;
        this.genero = genero;
        this.edicao = edicao;
        this.autor = autor;
    }
    /**
     * @param titulo the titulo to set
     */
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    /**
     * @return the genero
     */
    public String getGenero() {
        return genero;
    }
    /**
     * @param genero the genero to set
     */
    public void setGenero(String genero) {
        this.genero = genero;
    }
    /**
     * @return the edicao
     */
    public int getEdicao() {
        return edicao;
    }
    /**
     * @param edicao the edicao to set
     */
    public void setEdicao(int edicao) {
        this.edicao = edicao;
    }
    /**
     * @return the autor
     */
    public Autor getAutor() {
        return autor;
    }
    /**
     * @param autor the autor to set
     */
    public void setAutor(Autor autor) {
        this.autor = autor;
    }
    

}
