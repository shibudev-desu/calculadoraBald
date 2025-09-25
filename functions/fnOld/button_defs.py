import tkinter as tk
from functions.fnOld import all as ops
from functions.fnStranger import matheus as mth
from functions.fnNew.memoryFx import _sto, _rcl
from functions.fnNew.signals import swapSignals
import variables as var
from functions.fnStranger import Lucas as l
from functions.fnStranger import lynn as a
from functions.fnStranger.henrique import (Abc, Dc, ENG, Ln, Log, nCr, nPr, Pol, Rec, twoPoints)


def make_botoes(frame, controller):
    return [
        [
            ("", "SHIFT", (lambda: var.toggle_shift()), 7),
            ("", "ALPHA", (lambda: var.toggle_alpha()), 7),
            ("", "REPLAY", ops.nao_implementado, 7),
            # frame.display??
            ("CLR", "MODE", (lambda: l.toggle_mode(frame)), 7),
            ("", "ON", (lambda: ops.limpar_tudo(frame.display)), 7)
            ("", "ON", (lambda: ops.limpar_tudo(frame.display)), 7)
        ],

        [
            ("x!", "x⁻¹", (lambda: a.calc_inverso(frame.display) if not var.shift else a.calc_fatorial(frame.display)), 12),
            ("nPr", "nCr", ops.(lambda: ops.inserir("P", frame.display) if var.shift == True else ops.inserir("C", frame.display)), 12),
            ("   ", "    ", ops.ops.nao_implementado, 12),
            ("Rec( :", "Pol(", ops.ops.nao_implementado, 12),
            ("³√", "x³", (lambda: a.calc_cubo(frame.display) if not var.shift else a.calc_raiz_cubica(frame.display)), 12)
        ],

        [
            ("d/c", "ab/c", ops.nao_implementado, 7),
            ("", "√", (lambda: a.calc_raiz(frame.display)), 7),
            ("", "x²", (lambda: a.calc_quadrado(frame.display)), 7),
            ("x√", "^", (lambda: a.calc_exponenciacao(frame.display) if not var.shift else a.calc_radiciacao(frame.display)), 7),
            ("10^", "log", (lambda: ops.inserir("log(", frame.display)), 7),
            ("e^e", "ln", (lambda: ops.inserir("ln(", frame.display)), 7)
        ],

        [
            ("A", "(-)", (lambda: swapSignals(frame.display) if var.alpha == False else ops.nao_implementado()), 7),
            ("⭠ B", ".,, ,,", (lambda: ops.inserir("°", frame.display)), 7),
            ("hyp", "C", (lambda: mth.inserir_H() if not var.shift else ops.nao_implementado()), 7),
            ("sin⁻¹   D", "sin", (lambda: mth.inserir_sin() if not var.shift else mth.inserir_sin()), 7),
            ("cos⁻¹ E", "cos", (lambda: mth.inserir_cos() if not var.shift else mth.inserir_cos()), 7),
            ("tan⁻¹ F", "tan", (lambda: mth.inserir_tan() if not var.shift else mth.inserir_tan()), 7)
        ],

        [
            ("STO", "RCL", (lambda: _sto(frame.display, controller) if var.shift == True else _rcl(frame.display, controller)), 7),
            ("⭠", "ENG", ops.nao_implementado, 7),
            ("", "(", (lambda: ops.inserir("(", frame.display)), 7),
            ("x", ")", (lambda: ops.inserir(")", frame.display)), 7),
            (":     Y", ",", (lambda: ops.inserir(":" , frame.display) if var.shift is True else ops.inserir(",", frame.display)), 7),
            ("M- M", "M+", (lambda: l.func_m_plus()), 7)
        ],

        [
            ("", "7", (lambda: ops.inserir("7", frame.display)), 7),
            ("", "8", (lambda: ops.inserir("8", frame.display)), 7),
            ("", "9", (lambda: ops.inserir("9", frame.display)), 7),
            ("INS", "DEL", ops.nao_implementado, 7),
            ("OFF", "AC", ops.nao_implementado, 7)
        ],

        [
            ("", "4", (lambda: ops.inserir("4", frame.display)), 7),
            ("", "5", (lambda: ops.inserir("5", frame.display)), 7),
            ("", "6", (lambda: ops.inserir("6", frame.display)), 7),
            ("", "×", (lambda: ops.inserir("×", frame.display)), 7),
            ("", "÷", (lambda: ops.inserir("÷", frame.display)), 7)
        ],

        [
            ("S-SUM", "1", (lambda: ops.inserir("1", frame.display) if not var.shift else mth.ativar_menu_s_sum()), 7),
            ("SVAR", "2", (lambda: ops.inserir("2", frame.display) if not var.shift else mth.ativar_menu_s_var()), 7),
            ("", "3", (lambda: ops.inserir("3", frame.display)), 7),
            ("", "+", (lambda: ops.inserir("+", frame.display)), 7),
            ("", "-", (lambda: ops.inserir("-", frame.display)), 7)
        ],

        [
            ("Rnd", "0", (lambda: ops.inserir("0", frame.display) if not var.shift else ops.inserir("Rnd(", frame.display)), 7),
            ("Ran#", ".", (lambda: ops.inserir(".", frame.display) if not var.shift else ops.inserir("Ran#(", frame.display)), 7),
            ("π", "EXP", (lambda: mth.inserir_exp() if not var.shift else mth.inserir_pi()), 7),
            ("DRG+", "Ans", (lambda: mth.inserir_ans() if not var.shift else mth.ativar_menu_drg(frame.display)), 7),
            ("%", "=", (lambda: ops.calcular(frame.display, controller)), 7)
        ]
    ]