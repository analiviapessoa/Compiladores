# Análise de "operacoes.ll"
## Perguntas
1. Como estão representadas as funções soma, multiplica e calcula em IR?
R:  As funções estão representadas com o comando define, que inicia a definição de uma função no LLVM IR.
    Exemplo da função <soma>:
        <define dso_local i32 @soma(i32 noundef %0, i32 noundef %1) #0 {
            ...
        }>
    - Os parâmetros são %0 e %1 (com tipos explícitos i32). 
        - As variáveis são alocadas em <alloca>.
        - Os parâmetros são armazenados em <store> e depois carregados com <load> e a operação <add> realiza a soma.
        - O resultado é retornado com <ret>.
    - As funções <multiplica> e <calcula> seguem o mesmo padrão de <soma>, mas a primeria usa <mul> em vez de <add> e a segunda utiliza <icmp>, <br> e <call> para chamar <soma> ou <multiplica> 

2. O que aparece no IR que representa a condição if (valor > 10)?
R:  A condição if (valor > 10) aparece representada por estas instruções:
        %5 = icmp sgt i32 %4, 10        
        br i1 %5, label %6, label %9    
    - 1ª linha: Compara se %4 (valor) é maior que 10 usando signed greater than (sgt).
    - 2ª linha: Desvia condicionalmente:
        - Se verdadeiro, vai para o bloco %6 (<multiplica>).
        - Se falso, vai para o bloco %9 (<soma>).
    Ou seja, o <if> foi convertido em uma comparação (<icmp>) com um salto condicional (<br>).

3. Como são representadas as chamadas às funções auxiliares em IR?
R:  As chamadas são feitas com a instrução <call>, especificando o tipo de retorno, o nome da função, os argumentos e seus tipos.
    Exemplos de chamada: 
        <multiplica>: %8 = call i32 @multiplica(i32 noundef %7, i32 noundef 2)
            - %8 armazena o resultado da chamada.
            - Os argumentos são passados explicitamente com seus tipos.
        <soma>: %11 = call i32 @soma(i32 noundef %10, i32 noundef 5)        
        <printf>: %5 = call i32 (ptr, ...) @__mingw_printf(ptr noundef @.str, i32 noundef %4)

# Análise de "operacoes_mod.ll"
## Perguntas
1. Como o if (temp % 2 == 0) aparece no IR?
R:  Essa condição aparece representada pelas instruções abaixo dentro da função <calcula>:
        %8 = srem i32 %7, 2
        %9 = icmp eq i32 %8, 0
        br i1 %9, label %10, label %13
    - 1ª linha: Realiza o módulo (resto da divisão de temp por 2).
    - 2ª linha: Compara se o resultado do módulo é igual a zero (temp % 2 == 0).
    - 3ª linha: Faz o desvio condicional com base nessa comparação:
        - Se for verdadeiro (par), vai para o bloco %10
        - Se for falso (ímpar), vai para %13

2. Como o operador % (módulo) é representado no LLVM IR?
R:  O operador % (módulo) em C é representado no LLVM IR pela instrução <srem>, que significa Signed Remainder (resto da divisão com sinal)
    Exemplo: %8 = srem i32 %7, 2
    - %7 é o valor de temp
    - 2 é o divisor
    - %8 recebe o valor de temp % 2

3. Quais são os blocos básicos criados pela nova lógica condicional?
R:  A função <calcula> apresenta os seguintes blocos básicos relacionados à nova lógica condicional:
    - Bloco de entrada (implícito): onde <temp> é calculado:
        %5 = load i32, ptr %3, align 4
        %6 = call i32 @soma(i32 noundef %5, i32 noundef 3)
        store i32 %6, ptr %4, align 4
        %7 = load i32, ptr %4, align 4
        %8 = srem i32 %7, 2
        %9 = icmp eq i32 %8, 0
        br i1 %9, label %10, label %13
    - Bloco %10 (condição verdadeira → temp % 2 == 0):
        %11 = load i32, ptr %4, align 4
        %12 = call i32 @multiplica(i32 noundef %11, i32 noundef 4)
        store i32 %12, ptr %2, align 4
        br label %16
    - Bloco %13 (condição falsa → temp % 2 != 0):
        %14 = load i32, ptr %4, align 4
        %15 = call i32 @divide(i32 noundef %14, i32 noundef 2)
        store i32 %15, ptr %2, align 4
        br label %16
    - Bloco de saída %16:
        %17 = load i32, ptr %2, align 4
        ret i32 %17

# Análise de "operacoes_opt.ll"
## Perguntas
1. Que mudanças ocorreram na função main após a otimização?
R: A função main não sofreu mudanças visíveis porque o código é simples e pequeno.

2. Alguma função foi inlined (inserida diretamente)? Como identificar?
R: Não. Nenhuma das funções <soma>, <multiplica> ou <calcula> foi <inlined>.

3. Alguma variável intermediária foi eliminada? Por quê?
R: Não visivelmente. As variáveis intermediárias ainda estão presentes com uso explícito de <alloca>, <store> e <load>

# Análise do CFG
## Perguntas
1. Quantos blocos básicos você consegue identificar na função calcula?
R: A função calcula tem quatro blocos básicos, visíveis no CFG:
    - Bloco 1: Entrada, realiza soma, módulo e comparação (temp % 2 == 0)
    - Bloco 10: Executado se o if for verdadeiro → chama multiplica
    - Bloco 13: Executado se o if for falso → chama divide
    - Bloco 16: Bloco final que retorna o resultado

2. Quais são os caminhos possíveis a partir da condição if (temp % 2 == 0)?
R: A condição está representada no bloco 1:
        %8 = srem i32 %7, 2
        %9 = icmp eq i32 %8, 0
        br i1 %9, label %10, label %13
    - Se verdadeiro (temp % 2 == 0) → vai para bloco 10 (multiplica)
    - Se falso (temp % 2 != 0) → vai para bloco 13 (divide)
    Ambos os caminhos convergem no bloco 16, que carrega e retorna o resultado.

3. O fluxo de controle inclui blocos de erro ou casos não triviais (e.g., retorno precoce)?
R: Não. O fluxo é direto e controlado (sem <return> antecipadoe sem tratamento de exceções, <unreachable> ou blocos de erro).
   A função <divide> possui uma verificação (y == 0), mas isso é tratado dentro da própria função divide, não em <calcula>.

4. Há blocos com apenas instruções de salto? O que você imagina que isso indica?
R: Na função calcula, não há blocos com apenas salto. Todos os blocos contêm cálculo ou chamada de função, <store> e apenas depois um <br>.