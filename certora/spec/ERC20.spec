
methods {
    balanceOf(address) returns (uint) envfree
}

/// Transfer must move `amount` tokens from the caller's account to `recipient`
rule transferSpec {
    address sender; address recip; uint amount;

    env e;
    require e.msg.sender == sender;

    mathint balance_sender_before = balanceOf(sender);
    mathint balance_recip_before = balanceOf(recip);

    transfer(e, recip, amount);

    mathint balance_sender_after = balanceOf(sender);
    mathint balance_recip_after = balanceOf(recip);

    require sender != recip;

    assert balance_sender_after == balance_sender_before - amount,
        "transfer must decrease sender's balance by amount";

    assert balance_recip_after == balance_recip_before + amount,
        "transfer must increase recipient's balance by amount";
}


/// Transfer must revert if the sender's balance is too small
rule transferReverts {
    env e; address recip; uint amount;

    require balanceOf(e.msg.sender) < amount;

    transfer@withrevert(e, recip, amount);

    assert lastReverted,
        "transfer(recip,amount) must revert if sender's balance is less than `amount`";
}


/// Transfer must not revert unless
///    - sender doesn't have enough funds,
///    - or the message value is nonzero,
///    - or the recipient's balance would overflow,
///    - or the message sender is 0
///    - or the recipient is 0
///
/// @title Transfer doesn't revert
rule transferDoesntRevert {
    env e; address recipient; uint amount;

    require balanceOf(e.msg.sender) > amount;
    require e.msg.value == 0;
    require balanceOf(recipient) + amount < max_uint;
    require e.msg.sender != 0;
    require recipient != 0;

    transfer@withrevert(e, recipient, amount);
    assert !lastReverted;
}

rule transferFromSpec {
    // TODO!
    assert false, "rule not implemented";
}


rule transferFromReverts {
    // TODO!
    assert false, "rule not implemented";
}

rule transfer transferFromDoesntRevert {
    // TODO!
    assert false, "rule not implemented";
}

