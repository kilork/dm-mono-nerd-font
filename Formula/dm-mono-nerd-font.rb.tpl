class DmMonoNerdFont < Formula
  desc "DM Mono with Nerd Fonts glyphs"
  homepage "https://github.com/kilork/dm-mono-nerd-font"
  version "{{VERSION}}"

  url "https://github.com/kilork/dm-mono-nerd-font/releases/download/v{{VERSION}}/dm-mono-nerd-font-{{VERSION}}.tar.gz"
  sha256 "{{SHA256}}"

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