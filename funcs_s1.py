from datetime import datetime, timedelta

import pandas as pd

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calcular_b(B):
    """
    Função que calcula a Plaqueta (b) com base na fórmula b = B + 1.

    Inputs:
    B (float): Valor da coluna B.

    Outputs:
    Plaqueta (float): Valor calculado da Plaqueta (b).
    """

    plaqueta = B + 1
    return plaqueta

def calcular_k(J, L):
    """
    Função que calcula a variável C_EA.

    Inputs:
    J (float): Valor da coluna C_principal.
    L (float): Valor da coluna L.

    Outputs:
    C_EA (float): Resultado do produto entre C_principal e L.
    """
    C_EA = J * L
    return C_EA

def calcular_m(J, N):
    """
    Função que calcula a variável C_CA usando a fórmula m = J * N.

    Inputs:
    - J (float): Valor da coluna C_principal.
    - N (float): Valor da coluna N.

    Outputs:
    - C_CA (float): Resultado do cálculo da fórmula m = J * N.
    """
    C_CA = J * N
    return C_CA

def calcular_o(J, K, M):
    """
    Função que calcula a variável C_imob com base na fórmula: C_imob = J + K + M

    Parâmetros:
    J (float): Valor da coluna J (correspondente a C_principal)
    K (float): Valor da coluna K (correspondente a C_EA)
    M (float): Valor da coluna M

    Retorno:
    C_imob (float): Valor calculado da variável C_imob
    """
    C_imob = J + K + M
    return C_imob

def calcular_q(P, O):
    """
    Função que calcula o percentual q com base na fórmula q = P/O.

    Inputs:
    P (float): Valor da coluna C_JOA (numerador).
    O (float): Valor da coluna C_JOA (denominador).

    Outputs:
    q (float): Valor da coluna C_JOA%, calculado como P/O.
    """
    # Verificar se o denominador (O) é diferente de zero para evitar divisão por zero
    if O != 0:
        q = P / O
        return q
    else:
        # Em caso de denominador zero, retorna None
        return None
    
def calcular_r(R):
    """
    Função que calcula o Weighted Average Cost of Capital (WACC).

    Inputs:
    R (float): Representa o custo médio ponderado de capital (WACC).

    Outputs:
    r (float): O WACC calculado.
    """
    r = R
    return r

def calcular_u(o, t):
    """
    Função que calcula a variável u com base na fórmula do Excel: u = O * T

    Parâmetros:
    - o (float): Valor correspondente a C_imob (nome original na tabela).
        Descrição: Representa a porcentagem de ocupação de imóveis (C_imob) associada à variável O.
        Intervalo: Qualquer número real.

    - t (float): Valor correspondente a C_JOAR% (nome original na tabela).
        Descrição: Representa a taxa de ocupação ajustada para o ano (C_JOAR%) associada à variável T.
        Intervalo: Qualquer número real.

    Retorna:
    - u (float): Valor correspondente a C_JOAR (nome original na tabela).
        Descrição: Representa a variável resultante do produto entre a porcentagem de ocupação de imóveis (C_imob) e a taxa de ocupação ajustada para o ano (C_JOAR%).
        Intervalo: Qualquer número real.

    Exemplo de uso:
    >>> calcular_u(0.75, 0.95)
    0.7125
    """
    u = o * t
    return u

def calcular_v(O, U):
    """
    Função que calcula a variável V (CH) com base nas entradas O (C_imob) e U (C_JOAR).

    Parâmetros:
    - O (float): Valor da coluna O, representando a variável C_imob.
    - U (float): Valor da coluna U, representando a variável C_JOAR.

    Retorna:
    - CH (float): Valor calculado da variável CH (CH) usando a fórmula CH = O + U.
    """

    # Fórmula: CH = O + U
    CH = O + U

    return CH

def calcular_z(z):
    """
    Função que calcula a variável z (Data-base BRR) com base na fórmula z = Z.

    Parameters:
    z (float): Valor da variável Z.

    Returns:
    float: Valor calculado da variável z (Data-base BRR).

    Exemplo:
    >>> calcular_z(10.5)
    10.5
    """
    # A variável z (Data-base BRR) é simplesmente igual à variável Z.
    return z

def calcular_ab(Y):
    """
    Função que calcula a variável AB a partir da variável Y.

    Inputs:
    Y (float): Valor da variável Y.

    Outputs:
    ab (float): Resultado do cálculo da variável AB.
    
    Descrição:
    A variável AB é calculada utilizando a fórmula AB = Y, onde 'Y' representa
    a Data-base do laudo. O resultado é armazenado na variável AB.
    """
    ab = Y
    return ab

def calcular_ad(ac, aa):
    """
    Função que calcula o Delta IPCA de acordo com a fórmula do Excel: ad = ROUND(ac / aa - 1, 4)

    Parâmetros:
    - ac (float): Valor da coluna 'IPCA_final' na tabela.
    - aa (float): Valor da coluna 'IPCA_imob' na tabela.

    Saída:
    - ad (float): Resultado do cálculo do Delta IPCA arredondado para 4 casas decimais.
    
    Exemplo de Uso:
    ```python
    resultado = calcular_delta_ipca(2.5, 2.0)
    print(resultado)  # Saída esperada: 0.25
    ```
    """
    ad = round(ac / aa - 1, 4)
    return ad

def calcular_ae(V, AD):
    """
    Função que calcula a variável CHC usando a fórmula: CHC = V * (1 + AD)

    Inputs:
    - V (float): Valor da variável V (CH na fórmula original)
    - AD (float): Valor da variável AD (Delta_IPCA na fórmula original)

    Outputs:
    - CHC (float): Valor calculado da variável CHC usando a fórmula
    """
    CHC = V * (1 + AD)
    return CHC

def calcular_aj(ag, ah, ai):
    """
    Função que calcula a vida útil regulatória com base em uma condição.

    Inputs:
    ag (float): Prazo do contrato em anos.
    ah (float): Vida útil física em anos.
    ai (str): Vida útil regulatória (critério), deve ser "Contrato" ou "Nãodeprecia".

    Outputs:
    aj (float): Vida útil regulatória em anos, calculada com base na condição especificada na fórmula.
    """

    # Verifica se ai é "Contrato"
    if ai == "Contrato":
        aj = ag
    # Se ai não for "Contrato", verifica se é "Nãodeprecia"
    elif ai == "Não deprecia":
        aj = 0
    else:
        # Se ai não for nenhum dos valores esperados, assume o valor de ah
        aj = ah

    return aj

def calcular_ak(aj):
    """
    Função que calcula a Taxa de Depreciação Regulatória (TDR) com base na fórmula do Excel.

    Inputs:
    aj (float): Vida útil regulatória em anos.

    Outputs:
    ak (float): TDR anual calculada.
    """
    # Verifica se a vida útil regulatória é diferente de zero
    if aj != 0:
        # Calcula a TDR usando a fórmula do Excel
        ak = 1 / aj
    else:
        # Se a vida útil regulatória for zero, a TDR é definida como zero
        ak = 0
    
    return ak

def calcular_al(AK):
    """
    Função que calcula a Taxa de Desconto Racional (TDR) mensal a partir da TDR anual.

    Inputs:
    AK (float): Taxa de Desconto Racional (TDR) anual.

    Outputs:
    AL (float): Taxa de Desconto Racional (TDR) mensal calculada.
    """

    # Fórmula: AL = AK / 12
    AL = AK / 12

    return AL

def calcular_am(x, z, aj):
    """
    Função que calcula a variável AM (DeltaT_oper) com base na fórmula do Excel.

    Inputs:
    x (datetime): Data operacional.
    z (datetime): Data-base BRR.
    aj (float): Vida útil regulatória em anos.

    Outputs:
    am (float): DeltaT_oper em meses.
    """

    x = pd.to_datetime(x, format='%Y-%m-%d')
    z = pd.to_datetime(z, format='%Y-%m-%d')

    # Calcula a diferença em dias entre as datas x e z
    diff_days = (z - x).days

    # Calcula o valor da condição da fórmula
    condition_value = (z - x) / timedelta(days=365) * 12 > aj * 12

    # Aplica a lógica da fórmula usando a expressão condicional IF do Excel
    if condition_value:
        am = aj * 12
    else:
        am = diff_days / 365 * 12

    return am

def calcular_an(al, am, ae):
    """
    Função que calcula a variável DRA (an) com base na fórmula: DRA = AL * AM * AE

    Inputs:
    al (float): TDR (Taxa de Depreciação Residual) mensal
    am (float): DeltaT_oper (Delta de Tempo Operacional) em meses
    ae (float): Valor correspondente a AE (ou outra variável com significado semelhante)

    Outputs:
    dra (float): Resultado do cálculo da variável DRA
    """
    dra = al * am * ae
    return dra

def calcular_ao(AE, AN):
    """
    Função que calcula o CHC líquido com base nos valores de CHC e AN.

    Parâmetros:
    AE (float): Valor de CHC (colesterol HDL) na amostra.
    AN (float): Valor de DRA.

    Retorna:
    float: Valor do CHC líquido calculado (CHC - AN).
    """
    CHC_liquido = AE - AN
    return CHC_liquido


def calcular_at(z, AS):
    """
    Função que calcula a variável Delta_baixa com base na fórmula do Excel.

    Inputs:
    z (datetime): Data-base BRR
    AS (datetime): Data_baixa

    Outputs:
    at (float): Delta_baixa calculado
    """

    z = pd.to_datetime(z, format='%Y-%m-%d')
    as_ = pd.to_datetime(AS, format='%Y-%m-%d')

    # Verifica se o ano de Data-base BRR (z) é menor que o ano de Data_baixa (AS)
    if z.year < as_.year:
        at = 0
    else:
        # Calcula o Delta_baixa usando a fórmula (MONTH(AS) - 1) / 12
        at = (as_.month - 1) / 12

    return at

def calcular_au(ai):
    """
    Função que calcula a elegibilidade QRR com base na vida útil regulatória.

    Inputs:
    ai (str): Vida útil regulatória. Deve ser uma string indicando se o ativo deprecia.
             Valores possíveis: "Não deprecia" ou qualquer outro valor.

    Outputs:
    au (str): Elegibilidade QRR.
             Retorna "Não" se a vida útil regulatória for "Não deprecia", caso contrário, retorna "Sim".
    """
    if ai == "Não deprecia":
        au = "Não"
    else:
        au = "Sim"
    
    return au

def calcular_aw(i, x, z, ae, ao, ap, aq, ar, at, au):
    """
    Função que calcula a variável aw com base na fórmula do Excel fornecida.

    Inputs:
    - i: Quantitativo
    - x: Data oper
    - z: Data-base BRR
    - ae: CHC
    - ao: CHC_liquido
    - ap: IA
    - aq: Baixa
    - ar: Qtde_baixa
    - at: Delta_baixa
    - au: Elegível QRR

    Outputs:
    - aw: BRR_bruta
    """

    # Verificações condicionais conforme a fórmula do Excel
    if z > x:
        if au == "Sim":
            if ao > 0:
                if aq == "Sim":
                    if ar > i:
                        aw = 0
                    else:
                        aw = ae * ap * at + ae * ap * (1 - ar / i) * (1 - at)
                else:
                    aw = ae * ap
            else:
                aw = 0
        else:
            aw = 0
    else:
        aw = 0

    return aw

def calcular_ax(i, x, z, ao, ap, aq, ar, at, av):
    """
    Função que calcula a variável ax usando a fórmula do Excel fornecida.

    Inputs:
    - i (int): Quantitativo
    - x (float): Data oper
    - z (float): Data-base BRR
    - ao (float): CHC_liquido
    - ap (float): IA
    - aq (str): Baixa
    - ar (float): Qtde_baixa
    - at (float): Delta_baixa
    - av (str): Elegível juros

    Outputs:
    - ax (float): BRR_liquida

    Parâmetros:
    - i: Quantitativo representa a variável 'i'.
    - x: Data oper representa a variável 'x'.
    - z: Data-base BRR representa a variável 'z'.
    - ao: CHC_liquido representa a variável 'ao'.
    - ap: IA representa a variável 'ap'.
    - aq: Baixa representa a variável 'aq'.
    - ar: Qtde_baixa representa a variável 'ar'.
    - at: Delta_baixa representa a variável 'at'.
    - av: Elegível juros representa a variável 'av'.

    Exemplo de Uso:
    >>> resultado = calcular_ax(10, 5.0, 8.0, 100.0, 0.5, "Sim", 20.0, 0.1, "Sim")
    >>> print(resultado)
    42.0
    """
    if z > x:
        if av == "Sim":
            if ao > 0:
                if aq == "Sim":
                    if ar > i:
                        return 0
                    else:
                        return ao * ap * at + ao * ap * (1 - ar / i) * (1 - at)
                else:
                    return ao * ap
            else:
                return 0
        else:
            return 0
    else:
        return 0
    
def calcular_ay(ak, au, aw):
    """
    Função que calcula a variável QRR (anual) com base na fórmula do Excel.

    Inputs:
    ak (float): TDR (Taxa de Desconto Racional) anual.
    au (str): Elegível QRR (indicador de elegibilidade).
    aw (float): BRR_bruta (receita bruta base).

    Outputs:
    ay (float): QRR (anual) calculada.

    Parâmetros:
    - ak (float): Taxa de Desconto Racional anual, representando o atributo TDR.
    - au (str): Indicador de elegibilidade, representando o atributo Elegível QRR.
    - aw (float): Receita bruta base, representando o atributo BRR_bruta.
    
    Observações:
    - Se au for igual a "Sim", a fórmula será AW * AK; caso contrário, o resultado será 0.
    """
    if au == "Sim":
        ay = aw * ak
    else:
        ay = 0

    return ay

def calcular_az(av, ax, r):
    """
    Função que calcula os juros anuais com base nos parâmetros fornecidos.

    Parâmetros:
    av (str): Elegibilidade de juros. Deve ser "Sim" para ativar o cálculo de juros.
    ax (float): BRR_liquida.
    r (float): WACC (Custo Médio Ponderado de Capital).

    Retorna:
    float: Juros anuais calculados de acordo com a fórmula, ou 0 se av não for "Sim".
    """
    if av == "Sim":
        az = ax * r
    else:
        az = 0
    return az