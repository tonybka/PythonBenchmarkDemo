#!/usr/bin/env python3
# coding=utf-8
#########################################################################################
import os
import logging
import unittest
import time
from tempfile import NamedTemporaryFile
#########################################################################################
LOOP = 100000
ITERATIONS = 5
ROUNDS = 3
#########################################################################################


class computing_force():

    @staticmethod
    def sequence_loop(loopnum=LOOP):
        _sum = 0
        for i in xrange(loopnum):
            _sum += i
        return _sum

    @staticmethod
    def hash_seq_op(loop=LOOP):
        l = {}
        for i in xrange(loop):
            l['<<<%s>>>'%i] = i
        _sum = 0
        for i in xrange(loop):
            _sum += l['<<<%s>>>'%i]   


# def test_my_stuff():
#     logging.warning("====== Start test_my_stuff ======")
#     computing_force.sequence_loop()


def xrange(num):
    return iter(range(num))


def test_hash_seq_op(benchmark):
    benchmark.pedantic(computing_force.hash_seq_op, iterations=ITERATIONS, rounds=ROUNDS)

def test_sequence_loop(benchmark):
    ret = benchmark.pedantic(computing_force.sequence_loop, iterations=ITERATIONS, rounds=ROUNDS)
    assert ret == 4999950009 

