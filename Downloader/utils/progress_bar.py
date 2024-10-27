def mostrar_barra_progresso(completado, total, largura=50):
    percentual = completado / total
    barras = int(largura * percentual)
    espacos = largura - barras
    progresso_visual = f"[{'#' * barras}{'.' * espacos}] {percentual:.1%}"
    return progresso_visual
