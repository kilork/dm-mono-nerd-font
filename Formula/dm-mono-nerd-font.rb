class DmMonoNerdFont < Formula
  desc "DM Mono with Nerd Fonts glyphs"
  homepage "https://github.com/kilork/dm-mono-nerd-font"
  version "3.4.0"

  url "https://github.com/kilork/dm-mono-nerd-font/releases/download/v3.4.0/dm-mono-nerd-font-3.4.0.tar.gz"
  sha256 "84757679bef5b379364691a7d9995d03e9afa40c5cacc39e3cb428e4db1479a1"

  def install
    system "tar", "-xzf", cached_download, "--strip-components=1", "-C", prefix
  end

  def caveats
    <<~EOS
      Fonts are installed to #{prefix}.
      To make them available system-wide, copy to ~/Library/Fonts:
        cp #{prefix}/*.ttf ~/Library/Fonts/
    EOS
  end

  test do
  end
end