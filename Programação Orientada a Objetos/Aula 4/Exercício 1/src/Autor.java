public class Autor {
    private String nome, email, nacionalidade;

    /**
     * @param nome
     * @param email
     * @param nacionalidade
     */
    public Autor(String nome, String email, String nacionalidade) {
        this.nome = nome;
        this.email = email;
        this.nacionalidade = nacionalidade;
    }
    //Info
    public void info(){
        System.out.println("Nome do Autor: " + nome);
        System.out.println("E-mail do Autor: " + email);
        System.out.println("Nacionalidade do Autor: " + nacionalidade);
    }
    
    /**
     * @return the nome
     */
    public String getNome() {
        return nome;
    }
    
    /**
     * @param nome the nome to set
     */
    public void setNome(String nome) {
        this.nome = nome;
    }

    /**
     * @return the email
     */
    public String getEmail() {
        return email;
    }

    /**
     * @param email the email to set
     */
    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * @return the nacionalidade
     */
    public String getNacionalidade() {
        return nacionalidade;
    }

    /**
     * @param nacionalidade the nacionalidade to set
     */
    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    

}
