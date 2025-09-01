import tkinter as tk
from functions import operations_def as ops

def make_botoes(frame, controller, inserir, limpar_tudo, limpar_ultimo, calcular,
                nao_implementado, _sto, _rcl, var, changeDisplay):
    return [
        [
            ("", "SHIFT", (lambda: var.shiftTeorico()), 7),
            ("", "ALPHA", nao_implementado, 7),
            ("", "REPLAY", nao_implementado, 7),
            ("CLR", "MODE", nao_implementado, 7),
            ("", "ON", (lambda: limpar_tudo(frame.display)), 7)
        ],

        [
            ("x!", "x⁻¹", (lambda: ops.um_sobre_x(frame.display)), 12),
            ("nPr", "nCr", nao_implementado, 12),
            ("   ", "    ", nao_implementado, 12),
            ("Rec( :", "Pol(", nao_implementado, 12),
            ("³√", "x³", (lambda: ops.ao_cubo(frame.display)), 12)
        ],

        [
            ("d/c", "ab/c", nao_implementado, 7),
            ("", "√", (lambda: ops.calcular_raiz(frame.display)), 7),
            ("", "x²", (lambda: ops.ao_quadrado(frame.display)), 7),
            ("x√", "^", (lambda: inserir("^", frame.display)), 7),
            ("10^", "log", (lambda: inserir("log(", frame.display)), 7),
            ("e^ e", "ln", (lambda: inserir("ln(", frame.display)), 7)
        ],

        [
            ("A", "(-)", (lambda: changeDisplay(frame.display) if not var.AlphaUsado() else nao_implementado()), 7),
            ("⭠ B", ".,, ,,", nao_implementado, 7),
            ("hyp", "C", nao_implementado, 7),
            ("sin⁻¹   D", "sin", (lambda: inserir("sin(", frame.display)), 7),
            ("cos⁻¹ E", "cos", (lambda: inserir("cos(", frame.display)), 7),
            ("tan⁻¹ F", "tan", (lambda: inserir("tan(", frame.display)), 7)
        ],

        [
            ("STO", "RCL", (lambda: _sto(frame.display, controller) if var.ShiftUsado() else _rcl(frame.display, controller)), 7),
            ("⭠", "ENG", nao_implementado, 7),
            ("", "(", (lambda: inserir("(", frame.display)), 7),
            ("x", ")", (lambda: inserir(")", frame.display)), 7),
            (":     Y", ",", (lambda: inserir(":", frame.display) if var.ShiftUsado() else inserir(",", frame.display)), 7),
            ("M- M", "M+", nao_implementado, 7)
        ],

        [
            ("", "7", (lambda: inserir("7", frame.display)), 7),
            ("", "8", (lambda: inserir("8", frame.display)), 7),
            ("", "9", (lambda: inserir("9", frame.display)), 7),
            ("INS", "DEL", nao_implementado, 7),
            ("OFF", "AC", nao_implementado, 7)
        ],

        [
            ("", "4", (lambda: inserir("4", frame.display)), 7),
            ("", "5", (lambda: inserir("5", frame.display)), 7),
            ("", "6", (lambda: inserir("6", frame.display)), 7),
            ("", "×", (lambda: inserir("×", frame.display)), 7),
            ("", "÷", (lambda: inserir("÷", frame.display)), 7)
        ],

        [
            ("S-SUM", "1", (lambda: inserir("1", frame.display)), 7),
            ("SVAR", "2", (lambda: inserir("2", frame.display)), 7),
            ("", "3", (lambda: inserir("3", frame.display)), 7),
            ("", "+", (lambda: inserir("+", frame.display)), 7),
            ("", "-", (lambda: inserir("-", frame.display)), 7)
        ],

        [
            ("Rnd", "0", (lambda: inserir("Rnd(", frame.display) if var.ShiftUsado() else inserir("0", frame.display)), 7),
            ("Ran#", ".", (lambda: inserir("Ran#(", frame.display) if var.ShiftUsado() else inserir(".", frame.display)), 7),
            ("π", "EXP", nao_implementado, 7),
            ("DRG+", "Ans", nao_implementado, 7),
            ("%", "=", (lambda: calcular(frame.display, controller)), 7)
        ]
    ]